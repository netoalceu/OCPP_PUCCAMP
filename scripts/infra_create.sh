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
