#Criação do Container Base para testes do OCPP
#--cap-add=NET_ADMIN


FROM ubuntu:latest

# Camada de Infra para testes de rede
RUN apt-get update && apt-get install iproute2 net-tools iputils-ping\
    iperf tcpdump vim bridge-utils -y\
    && rm -rf /var/lib/apt/lists/*