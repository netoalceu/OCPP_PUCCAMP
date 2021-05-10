#!/bin/bash
echo
echo "====================================="
echo "    criando Volumes da Infra     "
echo "====================================="
docker volume create ocpp_log

echo
echo "====================================="
echo "   comando p criar o container qos   "
echo "====================================="
docker run -it -d \
    --name=qos \
    --network=net_cpo \
    --volume ocpp_log:/tmp \
    --cap-add=NET_ADMIN \
    netoalceu/infra:1.1 /bin/bash
docker network connect net_evse qos
echo
echo "====================================="
echo "   comando p criar o container cpo"
echo "====================================="
docker run -it -d\
    --name=cpo \
    --network=net_cpo \
    --volume ocpp_log:/app/log \
    --cap-add=NET_ADMIN \
    --env ADD_GATEWAY=192.168.10.1 \
    --env DEL_GATEWAY=192.168.10.254 \
    --env OCPP_APP=cpo_main.py \
    --rm \
    netoalceu/ocpp:1.0 /app/start.sh

echo
echo "====================================="
echo "  comando p criar o container EVSE"
echo "====================================="
echo "preparando CP_01"
docker run -d \
    --network=net_evse \
    --volume ocpp_log:/app/log \
    --cap-add=NET_ADMIN \
    --env CP_ID=CP_01 \
    --env CHARGER_URL="ws://192.168.10.2:9000/" \
    --workdir /app \
    --rm \
    netoalceu/ocpp:1.0 /app/start.sh
echo "Container OK"
echo
echo "preparando CP_02"
docker run -d \
    --network=net_evse \
    --volume ocpp_log:/app/log \
    --cap-add=NET_ADMIN \
    --env CP_ID=CP_02 \
    --env CHARGER_URL="ws://192.168.10.2:9000/" \
    --workdir /app \
    --rm \
    netoalceu/ocpp:1.0 /app/start.sh
echo "Container OK"
echo
echo "preparando CP_03"
docker run -d \
    --network=net_evse \
    --volume ocpp_log:/app/log \
    --cap-add=NET_ADMIN \
    --env CP_ID=CP_03 \
    --env CHARGER_URL="ws://192.168.10.2:9000/" \
    --workdir /app \
    --rm \
    netoalceu/ocpp:1.0 /app/start.sh
echo "Container OK"
echo
echo "preparando CP_04"
docker run -d \
    --network=net_evse \
    --volume ocpp_log:/app/log \
    --cap-add=NET_ADMIN \
    --env CP_ID=CP_04 \
    --env CHARGER_URL="ws://192.168.10.2:9000/" \
    --workdir /app \
    --rm \
    netoalceu/ocpp:1.0 /app/start.sh
echo "Container OK"
echo
echo "preparando CP_05"
docker run -d \
    --network=net_evse \
    --volume ocpp_log:/app/log \
    --cap-add=NET_ADMIN \
    --env CP_ID=CP_05 \
    --env CHARGER_URL="ws://192.168.10.2:9000/" \
    --workdir /app \
    --rm \
    netoalceu/ocpp:1.0 /app/start.sh
echo "Container OK"
echo
echo "preparando CP_06"
docker run -d \
    --network=net_evse \
    --volume ocpp_log:/app/log \
    --cap-add=NET_ADMIN \
    --env CP_ID=CP_06 \
    --env CHARGER_URL="ws://192.168.10.2:9000/" \
    --workdir /app \
    --rm \
    netoalceu/ocpp:1.0 /app/start.sh
echo "Container OK"
echo
echo "preparando CP_07"
docker run -d \
    --network=net_evse \
    --volume ocpp_log:/app/log \
    --cap-add=NET_ADMIN \
    --env CP_ID=CP_07 \
    --env CHARGER_URL="ws://192.168.10.2:9000/" \
    --workdir /app \
    --rm \
    netoalceu/ocpp:1.0 /app/start.sh
echo "Container OK"
echo
echo "preparando CP_08"
docker run -d \
    --network=net_evse \
    --volume ocpp_log:/app/log \
    --cap-add=NET_ADMIN \
    --env CP_ID=CP_08 \
    --env CHARGER_URL="ws://192.168.10.2:9000/" \
    --workdir /app \
    --rm \
    netoalceu/ocpp:1.0 /app/start.sh
echo "Container OK"
echo
echo "preparando CP_09"
docker run -d \
    --network=net_evse \
    --volume ocpp_log:/app/log \
    --cap-add=NET_ADMIN \
    --env CP_ID=CP_09 \
    --env CHARGER_URL="ws://192.168.10.2:9000/" \
    --workdir /app \
    --rm \
    netoalceu/ocpp:1.0 /app/start.sh
echo "Container OK"
echo
echo "preparando CP_10"
docker run -d \
    --network=net_evse \
    --volume ocpp_log:/app/log \
    --cap-add=NET_ADMIN \
    --env CP_ID=CP_10 \
    --env CHARGER_URL="ws://192.168.10.2:9000/" \
    --workdir /app \
    --rm \
    netoalceu/ocpp:1.0 /app/start.sh
echo "Container OK"
echo
