from datetime import datetime

cpo_ip = '0.0.0.0'
cpo_port = 9000
subprotocol = ['ocpp2.0']
evse_station_id = 'CP_1'
evse_url = 'ws://localhost:9000/'



def now():
    return datetime.utcnow().isoformat()


if __name__ == '__main__':
    print(type(now()))
    print(datetime.utcnow().isoformat())
    print(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z")

