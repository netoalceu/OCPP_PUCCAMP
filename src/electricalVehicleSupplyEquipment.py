import asyncio
from datetime import datetime

from ocpp.v20 import call
from ocpp.v20 import ChargePoint as cp


class EVSE(cp):
    ################## BOOT NOTIFICATION #################
    async def send_boot_notification(self):
        request = call.BootNotificationPayload(
                charging_station={
                    'model': 'Wallbox XYZ',
                    'vendor_name': 'anewone'
                },
                reason="PowerUp"
        )
        print(datetime.utcnow().isoformat(), 'Sent a BootNotification!')

        response = await self.call(request)
        if response.status == 'Accepted':
            print("Connected to central system.")
            await self.send_heartbeat(response.interval)

    ################## HEARTBEAT ##########################
    async def send_heartbeat(self, interval):
        request = call.HeartbeatPayload()
        while True:
            await self.call(request)
            print(datetime.utcnow().isoformat(), 'Sent a HeartBeat')
            await asyncio.sleep(interval)

