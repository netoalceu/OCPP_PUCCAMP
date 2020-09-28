import asyncio
from ocpp.v20 import call, ChargePoint as cp
from src.tools import now
from src.enumsV20 import *
from src.tools import now
from src.evse_class import evseClass

count = 0


class fsm:
    fim = 0
    init_state = 1
    authentication = 2
    start_transaction = 3
    measuring = 4
    stop_transaction = 5
    end_state = 6


async def init_state(info_do_carregador, protocol):  # Init State
    print(now(), 'Starting InitState')
    # Gerenciamento de Transições
    print(now(), 'Boot Notification is', info_do_carregador.flag_boot_notification)
    if not info_do_carregador.flag_boot_notification:
        return fsm.init_state
    return fsm.authentication


async def authentication(info_do_carregador, protocol):
    print(now(), 'Starting  Authentication')
    if await protocol.send_authorize(info_do_carregador.RFID_VALUE):
        print(now(), 'Authentication Approved')
        info_do_carregador.RFID_VALUE = '1212'
        return fsm.start_transaction
    else:
        print(now(), 'Authentication Denied')
        info_do_carregador.RFID_VALUE = '1234'
        return fsm.authentication


async def start_transaction(info_do_carregador, protocol):
    print(now(), 'Iniciando o  start_transaction')
    # Gerenciamento de Transições
    global count
    count = info_do_carregador.contador_numero_medicoes
    await protocol.send_request_start_transaction('123')
    return fsm.measuring


async def measuring(info_do_carregador, protocol):
    global count
    print(now(), 'Measuring...', count)
    await protocol.send_meter_values(1, now(), 100)
    if count <=0:
        return fsm.stop_transaction
    else:
        count -= 1
        return fsm.measuring


async def stop_transaction(info_do_carregador, protocol):
    print(now(), 'Iniciando o  StopTransaction')
    await protocol.send_request_stop_transaction('123')
    if info_do_carregador.ciclo_unico_da_maquina_de_estado:
        return fsm.end_state
    return fsm.authentication


async def end_state(info_do_carregador, protocol):  # end State
    print(now(), 'Iniciando o  end_state')
    info_do_carregador.parar_heartbeat = True
    await asyncio.sleep(2)
    protocol.fechar_arquivo_log()
    return fsm.fim


async def fim(info_do_carregador, protocol):  # end State
    print(now(), 'Iniciando o  end_state')
    await asyncio.sleep(2)
    return True


# Finite State Machine (FSM)
async def FSM(estado_do_carregador, info_do_carregador, protocol):
    switch = {
        0: fim,
        1: init_state,
        2: authentication,
        3: start_transaction,
        4: measuring,
        5: stop_transaction,
        6: end_state,
    }
    func = switch.get(estado_do_carregador)
    return await func(info_do_carregador, protocol)


async def state_machine_process(info_do_carregador, protocol):
    # Programa Principal
    estado_do_carregador = fsm.init_state
    await asyncio.sleep(2)
    while estado_do_carregador:
        estado_do_carregador = await FSM(estado_do_carregador, info_do_carregador, protocol)
        await asyncio.sleep(0.1)


if __name__ == '__main__':
    # Programa Principal
    from time import sleep

    estado_do_carregador = fsm.init_state
    info_do_carregador = evseClass()
    while estado_do_carregador:
        estado_do_carregador = FSM(estado_do_carregador, info_do_carregador)
        sleep(2)
