import datetime


def days_in_future(days: int):
    return datetime.datetime.now() + datetime.timedelta(days=days)
