import asyncio
import websockets
from src.electricalVehicleSupplyEquipment import EVSE
from src.evse_class import evseClass
from src.evse_state_machine import state_machine_process as smp
cp_id = ''


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
        await asyncio.gather(
            cs.start(),
            cs.send_boot_notification(carregador),
            smp(carregador),
        )


if __name__ == '__main__':
    print('Iniciando EVSE ' + cp_id)
    asyncio.run(main())
