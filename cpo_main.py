import asyncio
import websockets
from src.chargePointOperator import ChargePointOperator
from src.tools import now, CPO_IP, CPO_PORT, SUBPROTOCOL

async def on_connect(websocket, path):
    """
    Para cada novo ponto de carga que se conecta, cria-se uma nova instância
    EVSE e comeca a escutar as mensagens.
    """

    charge_point_id = path.strip('/')
    cp_created = ChargePointOperator(charge_point_id, websocket)
    print(now(), 'Conectando com EVSE ', charge_point_id)

    try:
        await cp_created.start()
    except:
        print(now(), 'Fim da conexão com ' + charge_point_id + '....')

async def main():
    server = await websockets.serve(
        on_connect,
        CPO_IP,
        CPO_PORT,
        subprotocols=SUBPROTOCOL
    )
    await server.wait_closed()

if __name__ == '__main__':
    print(now(), "Iniciando Servidor...")
    asyncio.run(main())
