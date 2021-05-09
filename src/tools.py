import os
from datetime import datetime
import time

CPO_IP = '0.0.0.0'
CPO_PORT = 9000
SUBPROTOCOL = ['ocpp2.0']
HEARTBEAT_INTERVAL = 10


def get_time():
    return time.time()


def now():
    return datetime.utcnow().isoformat()

def is_environ_exist(env):
    try:
        var = os.environ[env]
        return var
    except:
        return ""


if __name__ == '__main__':
    print(type(now()))
    print(datetime.utcnow().isoformat())
    print(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z")
