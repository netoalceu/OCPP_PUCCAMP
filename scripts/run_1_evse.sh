#!/bin/bash
echo "====================================="
echo "  comando p criar o container EVSE"
echo "====================================="
echo "preparando CP_Unico"
docker run -d \
    --network=net_evse \
    --volume ocpp_log:/app/log \
    --cap-add=NET_ADMIN \
    --env CP_ID=CP_Unico \
    --env CHARGER_URL="ws://192.168.10.2:9000/" \
    --workdir /app \
    --rm \
    netoalceu/ocpp:1.0 /app/start.sh
echo "Container OK"
echo
