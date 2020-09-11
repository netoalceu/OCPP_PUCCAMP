class evseClass:
    SUBPROTOCOL = ['ocpp2.0']
    CHARGER_URL = ''

    # Variaveis do EVSE para teste
    CP_ID = ''
    ENCODER = False
    CP_MODEL = ''
    CP_VENDOR = ''
    HEARTBEAT_INTERVAL = 0
    RFID_VALUE = ''
    CONNECTOR_ID = 0
    AUTHORIZED = False
    TRANSACTION_ID = 0
    TRANSACTION_STATUS = False
    METER_VALUES = 0
    CHARGING = False

    def __init__(self):
        self.CP_ID = 'CP_01'
        self.SUBPROTOCOL = ['ocpp2.0']
        self.CHARGER_URL = 'ws://localhost:9000/'

        # Variaveis do EVSE para teste
        self.ENCODER = True
        self.CP_MODEL = "openEVSE-V1"
        self.CP_VENDOR = "Alceu"
        self.HEARTBEAT_INTERVAL = 10
        self.RFID_VALUE = "1234"
        self.CONNECTOR_ID = 1
        self.AUTHORIZED = False
        self.TRANSACTION_ID = 1
        self.TRANSACTION_STATUS = False
        self.METER_VALUES = 0
        self.CHARGING = False
