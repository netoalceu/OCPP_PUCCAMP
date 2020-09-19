import asyncio
from ocpp.v20 import call, ChargePoint as cp
from src.tools import now
from src.enumsV20 import *


class EVSE(cp):
    ################## BOOT NOTIFICATION #################
    async def send_boot_notification(self, info_do_carregador):
        request = call.BootNotificationPayload(
            charging_station={
                'model': info_do_carregador.CP_MODEL,
                'vendor_name': info_do_carregador.CP_VENDOR
            },
            reason=BootReason.PowerUp
        )
        print(now(), 'BootNotification sent to CPO')
        response = await self.call(request)
        if response.status == RegistrationStatus.accepted:
            print(now(), 'BootNotification OK, connected with CPO.')
            info_do_carregador.HEARTBEAT_INTERVAL = response.interval
            info_do_carregador.flag_boot_notification = True
            await self.send_heartbeat(info_do_carregador)
        else:
            print(now(), 'BootNotification OK, did not connect with CPO.')
            import sys
            try:
                sys.exit(1)
            except:
                print("Closing EVSE... Bye")

    ################## HEARTBEAT ##########################
    async def send_heartbeat(self, info_do_carregador):
        request = call.HeartbeatPayload()
        while True:
            print(now(), 'HeartBeat sent to CPO')
            response = await self.call(request)
            if response.current_time:
                print(response.current_time, "Heartbeat delivered in CPO")
            else:
                print("Heartbeat not delivered")
            print(now(), "Heartbeat feedback in EVSE")
            await asyncio.sleep(info_do_carregador.HEARTBEAT_INTERVAL)
