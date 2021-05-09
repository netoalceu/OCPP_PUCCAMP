#Criação do Container Base para testes do OCPP
#--cap-add=NET_ADMIN


FROM ubuntu:latest

# Camada de Infra para testes de rede
RUN apt update && apt install -y iproute2 net-tools iputils-ping iperf tcpdump vim && rm -rf /var/lib/apt/lists/*