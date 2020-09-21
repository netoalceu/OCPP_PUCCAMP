import asyncio
from time import time

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

        #await asyncio.gather(cs.start(), evaluation(carregador, cs))


        await asyncio.gather(
            cs.start(),
            cs.send_boot_notification(carregador),
            smp(carregador, cs)
        )

if __name__ == '__main__':
    print('Iniciando EVSE ' + cp_id)
    asyncio.run(main())
