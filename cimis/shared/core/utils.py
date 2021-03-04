import datetime

def get_utc_timestamp():
    return datetime.datetime.utcnow()\
            .replace(tzinfo=datetime.timezone.utc)\
            .isoformat()