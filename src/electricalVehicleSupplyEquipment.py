import asyncio
from ocpp.v20 import call, ChargePoint as cp
from src.tools import now
from src.enumsV20 import *


class EVSE(cp):
    ################## BOOT NOTIFICATION #################
    async def send_boot_notification(self, cp_model, cp_vendor):
        request = call.BootNotificationPayload(
                charging_station={
                    'model': cp_model,
                    'vendor_name': cp_vendor
                },
                reason=BootReason.PowerUp
        )
        print(now(), 'BootNotification sent to CPO')
        response = await self.call(request)
        if response.status == RegistrationStatus.accepted:
            print(now(), 'BootNotification OK, connected with CPO.')
            await self.send_heartbeat(response.interval)
        else:
            print(now(), 'BootNotification OK, did not connect with CPO.')
            import sys
            try:
                sys.exit(1)
            except:
                print("Closing EVSE... Bye")

    ################## HEARTBEAT ##########################
    async def send_heartbeat(self, interval):
        request = call.HeartbeatPayload()
        while True:
            print(now(), 'HeartBeat sent to CPO')
            response = await self.call(request)
            if response.current_time:
                print(response.current_time, "Heartbeat delivered in CPO")
            else:
                print("Heartbeat not delivered")
            print(now(), "Heartbeat feedback in EVSE")
            await asyncio.sleep(interval)
