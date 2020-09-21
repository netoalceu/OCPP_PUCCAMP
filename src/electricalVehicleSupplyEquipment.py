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

    ################## AUTHORIZE ##########################
    async def send_authorize(self, id):
        request = call.AuthorizePayload(
            id_token={
                'id_token': id,
                'type': IdTokenEnumType.ISO14443
            })
        response = await self.call(request)
        if response.id_token_info['status'] == RegistrationStatus.accepted:
            return True
        else:
            return False

    ################## START TRANSACTION ##########################
    async def send_request_start_transaction(self, id):
        request = call.RequestStartTransactionPayload(
            id_token={
                "id_token": str(id),
                "type": IdTokenEnumType.ISO14443
            },
            remote_start_id=1
        )
        response = await self.call(request)
        if response.status == AvailabilityStatus.accepted:
            print(now(), 'Start Transaction Accepted')
            return True
        else:
            print(now(), 'Start Transaction rejected')
            return False

    ################## METER VALUES ##########################
    async def send_meter_values(self, evse_id, timestamp, met_value):
        meter_array = []
        meter_array.append({
            "timestamp": timestamp,
            "sampledValue": [
                {"value": 100}]
        })
        request = call.MeterValuesPayload(
            evse_id=123,
            meter_value=meter_array
        )
        response = await self.call(request)

        if response:
            print("Meter values sent")
        else:
            print("Error in central system with meter values")

    ################## STOP TRANSACTION ##########################
    async def send_request_stop_transaction(self, id):
        request = call.RequestStopTransactionPayload(
            transaction_id=str(id)
        )
        response = await self.call(request)
        if response:
            print("Stop transaction ")
            # return False to turn off transaction status
            return False
        else:
            print("Error Stopping transaction")
            return True
