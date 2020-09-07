import asyncio
import websockets
from src.electricalVehicleSupplyEquipment import EVSE
from src.tools import CHARGER_URL, SUBPROTOCOL, CP_ID, CP_MODEL, CP_VENDOR


async def main():
    """
    Inicializa-se os EVSEs individualmente. Sendo necessario somente
    a mudança do CHARGER_ID.
    """
    async with websockets.connect(
            CHARGER_URL + CP_ID,
            subprotocols=SUBPROTOCOL
    ) as ws:
        cs = EVSE(CP_ID, ws)
        await asyncio.gather(cs.start(), cs.send_boot_notification(
            CP_MODEL,
            CP_VENDOR))


if __name__ == '__main__':
    print('Iniciando EVSE ' + CP_ID)
    asyncio.run(main())
