#!/bin/bash
echo "Apagando TODOS os Containers em operação..."
docker container rm $(docker container ls -a -q) -f

echo "Apagando o volume de dados OCPP..."
docker volume rm ocpp_log

echo "Subindo infra de testes..."
./infra_create.sh

echo "resetando QoS..."
docker exec -d qos slow.sh reset
QOS=$1
export QOS
# echo $QOS
docker exec -d qos slow.sh $1
read -p 'Check se o QoS e o TCPDUMP estão ok e Pressione uma tecla p continuar'

docker exec -d qos tcpdump -i eth0 -w /tmp/$1.pcap

echo "Subindo EVSEs..."
./run_50_evse.sh

read -p 'ATTACH o CONTAINER CPO para monitorar o teste e Pressione uma tecla p continuar'

docker cp qos:/tmp /home/alceu/workspace/OCPP_PUCCAMP/resultados/app_docker/$1
cat ~/workspace/OCPP_PUCCAMP/resultados/app_docker/*$1/*txt > ~/workspace/OCPP_PUCCAMP/resultados/app_docker/*$1/$1_merge.txt
clear

echo 'Script Finalizado'
