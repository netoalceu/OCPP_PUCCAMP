import asyncio
from ocpp.v20 import call, ChargePoint as cp
from src.tools import now
from src.enumsV20 import *


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
        print(now(), 'Sent a BootNotification!')

        response = await self.call(request)
        if response.status == RegistrationStatus.accepted:
            print("Connected to central system.")
            await self.send_heartbeat(response.interval)

    ################## HEARTBEAT ##########################
    async def send_heartbeat(self, interval):
        request = call.HeartbeatPayload()
        while True:
            await self.call(request)
            print(now(), 'Sent a HeartBeat')
            await asyncio.sleep(interval)

