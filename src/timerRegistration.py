from datetime import datetime


def now():
    return datetime.utcnow().isoformat()


if __name__ == '__main__':
    print(type(now()))
    print(datetime.utcnow().isoformat())
    print(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z")
