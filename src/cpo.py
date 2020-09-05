import asyncio

try:
    import websockets
except ModuleNotFoundError:
    print(" websocket lib - instalar biblioteca")
    import sys
    sys.exit(1)

from chargePointOperator import ChargePointOperator

valid_tokens = ["a36ef7b0", "1234", "12345", "1111", "2222", 987]


async def on_connect(websocket, path):
    """ For every new charge point that connects, create a ChargePoint instance
    and start listening for messages.
    """
    charge_point_id = path.strip('/')
    cp_created = ChargePointOperator(charge_point_id, websocket)
    print(charge_point_id)

    await cp_created.start()


async def main():
    server = await websockets.serve(
        on_connect,
        '0.0.0.0',
        9000,
        subprotocols=['ocpp 2.0']
    )

    await server.wait_closed()


if __name__ == '__main__':
    print("Iniciando Servidor...")
    try:
        print("...com Python version 3.7 or more")
        asyncio.run(main())
    except AttributeError:
        print("...com Python version 3.6 or less")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()
