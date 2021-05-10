#Criação do Container Base para testes do OCPP
#--cap-add=NET_ADMIN


FROM netoalceu/infra:1.1

# Camada de Infra para testes de rede
RUN apt update && apt install -y python3-pip -y && pip3 install asyncio==3.4.3 \
    websockets==8.1 \
    ocpp==0.6.4 \
    aiohttp==3.6.2 \
    websocket==0.2.1 \
    SimpleWebSocketServer==0.1.1 \
    jsonschema==3.2.0 && rm -rf /var/lib/apt/lists/*

# Camadas de copia de arquivos e diretorios app
COPY /src /app/src
COPY cpo_main.py /app
COPY evse_main.py /app
COPY /scripts/start.sh /app

#Variaveis de Ambiente EVSE (Padrão)
ENV CHARGER_URL="ws://172.17.0.2:9000/"
ENV QNT_METER=1000
ENV CP_ID=CP_Base
ENV ADD_GATEWAY=192.168.20.1
ENV DEL_GATEWAY=192.168.20.254
ENV OCPP_APP=evse_main.py

WORKDIR /app

