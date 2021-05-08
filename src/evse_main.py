import asyncio
import sys
import os

import websockets
from src.electricalVehicleSupplyEquipment import EVSE
from src.evse_class import evseClass
from src.evse_state_machine import state_machine_process as smp
from src.tools import now

cp_id = ''


async def evaluation(info_do_carregador, protocol):
    print('inicio de avaliação de funções de teste')
    while True:
        await protocol.send_authorize('1234')
        await protocol.send_meter_values(1, now(), 100)
        await protocol.send_request_start_transaction('123')
        await protocol.send_request_stop_transaction('123')
        await asyncio.sleep(2)

async def func_check_to_close(info_do_carregador,protocol):
    print('inicio de avaliação de funções de teste')
    while True:
        await asyncio.sleep(0.1)
        if info_do_carregador.heartbeat_parado and info_do_carregador.fsm_parado:
            loop = asyncio.get_event_loop
            loop.run_until_complete (main())
            loop.close()


async def main():
    """
    Inicializa-se os EVSEs individualmente. Sendo necessario somente
    a mudança do CHARGER_ID.
    """
    global cp_id
    carregador = evseClass()
    cp_id = carregador.CP_ID
    async with websockets.connect(
            carregador.CHARGER_URL + carregador.CP_ID,
            subprotocols=carregador.SUBPROTOCOL
    ) as ws:
        cs = EVSE(carregador.CP_ID, ws)

        start = cs.start()
        boot_notification = cs.send_boot_notification(carregador)
        state_machine = smp(carregador, cs)
        check_to_close = func_check_to_close(carregador, cs)

        # await asyncio.gather(cs.start(), evaluation(carregador, cs))
        await asyncio.gather(
            start,
            boot_notification,
            state_machine,
            check_to_close

        )
        """
        await asyncio.gather(
            cs.start(),
            cs.send_boot_notification(carregador)
        )
        """

if __name__ == '__main__':
    print('Iniciando EVSE ' + cp_id)
    try:
        asyncio.run(main())
        print("so para testar")
    except:
        print(now(), 'Fechando EVSE ' + cp_id)
