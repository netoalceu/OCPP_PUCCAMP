#Criação do Container Base para testes do OCPP
#--cap-add=NET_ADMIN


FROM netoalceu/infra:1.0

# Camada de Infra para testes de rede
RUN apt update && apt install -y python3-pip -y && pip3 install asyncio==3.4.3 websockets==8.1 ocpp==0.6.4 aiohttp==3.6.2 websocket==0.2.1 SimpleWebSocketServer==0.1.1 jsonschema==3.2.0 && rm -rf /var/lib/apt/lists/*