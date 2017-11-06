import random
from datetime import datetime, timedelta


def all_even_numbers():
    for i in range(0,100,2):
        yield i


def random_increasing_number(start_from = 0):
    last_num = start_from
    next_num = random.randint(last_num, last_num + 150)
    while True:
        next_num = random.randint(next_num, next_num+150)
        yield next_num


def next_day():
    i = 0
    today = datetime.datetime.today().date()

    while True:
        yield today
        today = today + datetime.timedelta(days=i)
        i += 1
