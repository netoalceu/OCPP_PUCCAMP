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
    netoalceu/ocpp:1.0 /bin/bash
echo "====================================="
echo "  comando p criar o container EVSE"
echo "====================================="
echo "preparando CP_Unico"
docker run -it -d \
    --network=net_evse \
    --volume ocpp_log:/app/log \
    --cap-add=NET_ADMIN \
    --env CP_ID=CP_Unico \
    --env CHARGER_URL="ws://192.168.10.2:9000/" \
    --workdir /app \
    --rm \
    netoalceu/ocpp:1.0 /bin/bash
echo "Container OK"
echo
read -p 'ATTACH o CONTAINER CPO para monitorar o teste e Pressione uma tecla p continuar'

docker cp qos:/tmp /home/alceu/workspace/OCPP_PUCCAMP/resultados/teste/$1

read -p 'Pressione uma tecla p derrubar os containers'
echo "Apagando TODOS os Containers em operação..."
docker container rm $(docker container ls -a -q) -f

echo "Apagando o volume de dados OCPP..."
docker volume rm ocpp_log

