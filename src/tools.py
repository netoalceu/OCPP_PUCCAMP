from datetime import datetime

CP_ID = 'CP_1'
CPO_IP = '0.0.0.0'
CPO_PORT = 9000
SUBPROTOCOL = ['ocpp2.0']
CHARGER_URL = 'ws://localhost:9000/'

# Variaveis do EVSE para teste
ENCODER = True
CP_MODEL = "openEVSE-V1"
CP_VENDOR = "Alceu"
HEARTBEAT_INTERVAL = 10
RFID_VALUE = "1234"
CONNECTOR_ID = 1
AUTHORIZED = False
TRANSACTION_ID = 1
TRANSACTION_STATUS = False
METER_VALUES = 0
CHARGING = False

def now():
    return datetime.utcnow().isoformat()


if __name__ == '__main__':
    print(type(now()))
    print(datetime.utcnow().isoformat())
    print(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z")

