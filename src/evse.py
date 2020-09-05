import asyncio

try:
    import websockets
except ModuleNotFoundError:
    print(" websocket lib - instalar biblioteca")
    import sys

    sys.exit(1)

from electricalVehicleSupplyEquipment import EVSE

charge_point_id = 'CP_1'
url = 'ws://localhost:9000'

async def main():
    async with websockets.connect(
            url+'/'+charge_point_id,
            subprotocols=['ocpp2.0']
    ) as ws:
        evse = EVSE(charge_point_id, ws)

        await asyncio.gather(evse.start(), evse.send_boot_notification())


if __name__ == '__main__':
    print("Iniciando EVSE...")
    try:
        print("...com Python version 3.7 or more")
        asyncio.run(main())
    except AttributeError:
        print("...com Python version 3.6 or less")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()
