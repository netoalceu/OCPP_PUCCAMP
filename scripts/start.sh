#!/bin/bash
echo
echo "======================"
echo "    checando IP       "
echo "======================"
echo
ifconfig |grep inet
echo
echo "======================"
echo "    roteando rede     "
echo "======================"
echo
echo on
route
echo
route add default gw $ADD_GATEWAY
route del default gw $DEL_GATEWAY
route
echo off

echo
echo "======================"
echo "  iniciando sistema   "
echo "======================"
echo

python3 $OCPP_APP

echo
echo "======================"
echo "  Salvando log    "
echo "======================"
echo
mv log.txt ./log/$CP_ID.txt