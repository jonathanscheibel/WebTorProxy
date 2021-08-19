import os
from time import sleep
from urllib import request
from datetime import datetime
import subprocess
from db import select


def execute_not_licencied():
    os.system("poweroff")


def is_date_limit():
    web = "https://jonathanscheibel.github.io/clientes/2021010001/chave/liberacao.html"
    file = request.urlopen(web)
    data_web = file.read().decode("utf-8").strip()
    date_limit = datetime.strptime(data_web, '%d/%m/%Y').date()
    proc = subprocess.Popen(["wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d\' \' -f5-7"],
                            stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    actual_date = datetime.strptime(out.decode("utf-8").strip(), '%d %b %Y').date()
    return actual_date < date_limit


def is_into_limit():
    LIMIT_LICENCE = 1000
    return int(select('SELECT count(token) from change')[0]) <= LIMIT_LICENCE


def check_all_validates():
    A_TIMER = 300
    ERRORS_LIMIT = 1200
    errors = 0
    while True:
        try:
            if not is_date_limit():
                execute_not_licencied()
            if not is_into_limit():
                execute_not_licencied()
            errors = 0
            sleep(A_TIMER)
        except:
            errors += 1
            sleep(A_TIMER)
            if errors >= ERRORS_LIMIT:
                execute_not_licencied()
                exit()


check_all_validates()