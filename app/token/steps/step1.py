import os
from time import sleep
from urllib import request
from datetime import datetime


def is_date_limit():
    web = "https://jonathanscheibel.github.io/clientes/2021010001/chave/liberacao.html"
    try:
        file = request.urlopen(web)
        data_web = file.read().decode("utf-8").strip()
        date_limit = datetime.strptime(data_web, '%d/%m/%Y').date()
        os.system("ntpdate a.ntp.br b.ntp.br c.ntp.br > /dev/null")
        return datetime.today().date() < date_limit
    except:
        return False


def step1():
    while True:
        if not is_date_limit():
            os.system("poweroff")
        sleep(1800)


step1()