import datetime
def add_gigasecond(birth_date):
    sec=birth_date.timestamp()
    sec+=1000000000
    return datetime.datetime.fromtimestamp(sec)
