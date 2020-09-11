from datetime import datetime

CPO_IP = '0.0.0.0'
CPO_PORT = 9000
SUBPROTOCOL = ['ocpp2.0']
HEARTBEAT_INTERVAL = 10

def now():
    return datetime.utcnow().isoformat()


if __name__ == '__main__':
    print(type(now()))
    print(datetime.utcnow().isoformat())
    print(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z")

