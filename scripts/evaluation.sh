#!/bin/bash
echo "Apagando TODOS os Containers em operação..."
docker container rm $(docker container ls -a -q) -f

echo "Apagando o volume de dados OCPP..."
docker volume rm ocpp_log

echo "Subindo infra de testes..."
./infra_create.sh

echo "resetando QoS..."
docker exec -d qos slow.sh reset
# read -p 'Pressione uma tecla p continuar'
QOS=$1
export QOS
# echo $QOS
docker exec -d qos slow.sh $1

echo "Subindo EVSEs..."
./run_10_evse.sh
