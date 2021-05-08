import asyncio

from ocpp.v20 import call, ChargePoint as cp
from src.tools import now, get_time as gt
from src.enumsV20 import *


class EVSE(cp):

    def __init__(self, id, connection, response_timeout=30):
        super().__init__(id, connection, response_timeout)
        self.arquivo = open('log.txt', 'w')
        self.arquivo.close()
        self.abrir_arquivo_log()
        self.tempo_inicial = 0

    def abrir_arquivo_log(self):
        self.arquivo = open('log.txt', 'a')
        return True

    def iniciar_timer_log(self):
        self.tempo_inicial = gt()
        return True

    def escrever_arquivo_log(self, funcao):
        log = f'{now()};{funcao};{(gt() - self.tempo_inicial) * 1000}\n'
        print(log)
        self.arquivo.write(log)
        return True

    def fechar_arquivo_log(self):
        return self.arquivo.close()

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
        self.iniciar_timer_log()
        response = await self.call(request)
        self.escrever_arquivo_log('send_boot_notification')
        if response.status == RegistrationStatus.accepted:
            print(now(), 'BootNotification OK, connected with CPO.')
            info_do_carregador.HEARTBEAT_INTERVAL = response.interval
            info_do_carregador.flag_boot_notification = True
            return await self.send_heartbeat(info_do_carregador)
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
        while not info_do_carregador.parar_heartbeat:
            print(now(), 'HeartBeat sent to CPO')
            self.iniciar_timer_log()
            response = await self.call(request)
            self.escrever_arquivo_log('send_heartbeat')

            if response.current_time:
                print(response.current_time, "Heartbeat delivered in CPO")
            else:
                print(now(), "Heartbeat not delivered")
            print(now(), "Heartbeat feedback in EVSE")
            await asyncio.sleep(info_do_carregador.HEARTBEAT_INTERVAL)
        info_do_carregador.heartbeat_parado = True
        return True
    ################## AUTHORIZE ##########################
    async def send_authorize(self, id):
        request = call.AuthorizePayload(
            id_token={
                'id_token': id,
                'type': IdTokenEnumType.ISO14443
            })
        self.iniciar_timer_log()
        response = await self.call(request)
        self.escrever_arquivo_log('send_authorize')
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
        self.iniciar_timer_log()
        response = await self.call(request)
        self.escrever_arquivo_log('send_request_start_transaction')
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
        self.iniciar_timer_log()
        response = await self.call(request)
        self.escrever_arquivo_log('send_meter_values')
        if response:
            print(now(), "Meter values sent")
        else:
            print(now(), "Error in central system with meter values")

    ################## STOP TRANSACTION ##########################
    async def send_request_stop_transaction(self, id):
        request = call.RequestStopTransactionPayload(
            transaction_id=str(id)
        )
        self.iniciar_timer_log()
        response = await self.call(request)
        self.escrever_arquivo_log('send_request_stop_transaction')
        if response:
            print(now(), "Stop transaction")
            # return False to turn off transaction status
            return False
        else:
            print(now(), "Error Stopping transaction")
            return True
