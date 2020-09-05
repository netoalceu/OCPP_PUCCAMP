import asyncio

try:
    import websockets
except ModuleNotFoundError:
    print(" websocket lib - instalar biblioteca")
    import sys

    sys.exit(1)

from datetime import datetime

from ocpp.routing import on, after
from ocpp.v20 import ChargePoint as cp
from ocpp.v20 import call_result
from ocpp.v16.enums import *

valid_tokens = ["a36ef7b0", "1234", "12345", "1111", "2222", 987]


class ChargePointOperator(cp):
    ################## BOOT NOTIFICATION #################
    @on('BootNotification')
    def on_boot_notification(self, charging_station, reason, **kwargs):
        print(datetime.utcnow().isoformat(), 'Got a BootNotification!')
        return call_result.BootNotificationPayload(
            current_time=datetime.utcnow().isoformat(),
            interval=10,
            status='Accepted'
        )

    @after('BootNotification')
    def after_boot_notification(self, charging_station, reason, **kwargs):
        print("Boot Notification from:")
        print("ChargePoint Vendor: ", charging_station)
        print("ChargePoint Model: ", reason)

    ################## HEARTBEAT ##########################
    @on('Heartbeat')
    def on_heartbeat(self):
        print(datetime.utcnow().isoformat(), 'On a Heartbeat!')
        return call_result.HeartbeatPayload(
            current_time=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z"
        )

    @after('Heartbeat')
    def after_heartbeat(self):
        print(datetime.utcnow().isoformat(), 'After - Heartbeat')
async def on_connect(websocket, path):
    """ For every new charge point that connects, create a ChargePoint instance
    and start listening for messages.
    """
    charge_point_id = path.strip('/')
    cp_created = ChargePointOperator(charge_point_id, websocket)

    await cp_created.start()


async def main():
    server = await websockets.serve(
        on_connect,
        '0.0.0.0',
        9000,
        subprotocols=['ocpp 2.0']
    )

    await server.wait_closed()


if __name__ == '__main__':
    print("Iniciando Servidor.....")
    try:
        print("Python version 3.7 or more")
        asyncio.run(main())
    except AttributeError:
        print("Python version 3.6 or less")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()
