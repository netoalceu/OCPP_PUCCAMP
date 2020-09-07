import asyncio
from src.tools import *

try:
    import websockets
except ModuleNotFoundError:
    print(" websocket lib - instalar biblioteca")
    import sys

    sys.exit(1)

from src.electricalVehicleSupplyEquipment import EVSE


async def main():
    async with websockets.connect(
            evse_url + evse_station_id,
            subprotocols=subprotocol
    ) as ws:
        cs = EVSE(evse_station_id, ws)

        await asyncio.gather(cs.start(), cs.send_boot_notification())


if __name__ == '__main__':
    print("Iniciando EVSE...")
    try:
        print("...com Python version 3.7 or more")
        asyncio.run(main())
    except AttributeError:
        print("...com Python version 3.6 or less")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()
