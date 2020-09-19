import asyncio
from ocpp.v20 import call, ChargePoint as cp
from src.tools import now
from src.enumsV20 import *
from src.tools import now
from src.evse_class import evseClass

count = 0


class fsm:
    end_state = 0
    init_state = 1
    authentication = 2
    start_transaction = 3
    measuring = 4
    stop_transaction = 5


def init_state(info_do_carregador):  # Init State
    print(now(),'Iniciando o  InitState')
    # Gerenciamento de Transições
    print(now(), 'Boot Notification is', info_do_carregador.flag_boot_notification)
    if not info_do_carregador.flag_boot_notification:
        return fsm.init_state
    return fsm.authentication


def authentication(info_do_carregador):
    print(now(), 'Iniciando o  Authentication')
    # Gerenciamento de Transições
    return fsm.start_transaction


def start_transaction(info_do_carregador):
    print(now(), 'Iniciando o  start_transaction')
    # Gerenciamento de Transições
    global count
    count = 0
    return fsm.measuring


def measuring(info_do_carregador):
    global count
    print(now(), 'Measuring...', count)
    # Gerenciamento de Transições
    if count >= 2:
        return fsm.stop_transaction
    else:
        count += 1
        return fsm.measuring


def stop_transaction(info_do_carregador):
    print(now(), 'Iniciando o  StopTransaction')
    # Gerenciamento de Transições
    return fsm.authentication


def end_state(info_do_carregador):  # end State
    print(now(), 'Iniciando o  end_state')
    return fsm.init_state


# Finite State Machine (FSM)
def FSM(estado_do_carregador, info_do_carregador):
    switch = {
        0: end_state,
        1: init_state,
        2: authentication,
        3: start_transaction,
        4: measuring,
        5: stop_transaction,
    }
    func = switch.get(estado_do_carregador, lambda: None)
    return func(info_do_carregador)


async def state_machine_process(info_do_carregador):
    # Programa Principal
    estado_do_carregador = fsm.init_state
    await asyncio.sleep(1)
    while estado_do_carregador:
        estado_do_carregador = FSM(estado_do_carregador, info_do_carregador)
        await asyncio.sleep(1)

if __name__ == '__main__':
    # Programa Principal
    from time import sleep
    estado_do_carregador = fsm.init_state
    info_do_carregador = evseClass()
    while estado_do_carregador:
        estado_do_carregador = FSM(estado_do_carregador, info_do_carregador)
        sleep(2)
