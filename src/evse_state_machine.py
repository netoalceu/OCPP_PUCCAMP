from time import sleep
count = 0

class fsm:
    end_state = 0
    init_state = 1
    authentication = 2
    start_transaction = 3
    measuring = 4
    stop_transaction = 5


def init_state():  # Init State
    print('Iniciando o  InitState')
    # Gerenciamento de Transições
    sleep(0.1)
    return fsm.authentication


def authentication():
    print('Iniciando o  Authentication')
    # Gerenciamento de Transições
    sleep(0.1)
    return fsm.start_transaction


def start_transaction():
    print('Iniciando o  start_transaction')
    # Gerenciamento de Transições
    sleep(0.1)
    return fsm.measuring


def measuring():
    global count
    print('Iniciando o  Measuring', count)
    # Gerenciamento de Transições
    sleep(0.1)
    if count >= 2:
        return fsm.stop_transaction
    else:
        count += 1
        return fsm.measuring


def stop_transaction():
    print('Iniciando o  StopTransaction')
    # Gerenciamento de Transições
    sleep(0.1)
    return fsm.authentication


def end_state():  # end State
    print('Iniciando o  end_state')
    sleep(0.1)
    return fsm.init_state


# Finite State Machine (FSM)
def FSM(estado):
    switch = {
        0: end_state,
        1: init_state,
        2: authentication,
        3: start_transaction,
        4: measuring,
        5: stop_transaction,
    }
    func = switch.get(estado, lambda: None)
    return func()


# Programa Principal
estado = fsm.init_state
while estado:
    estado = FSM(estado)
    sleep(2)
