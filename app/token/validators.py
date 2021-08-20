import psutil
import os


def is_running(script):
    for q in psutil.process_iter():
        if q.name().startswith('python'):
            if len(q.cmdline()) > 1 and script in q.cmdline()[1] and q.pid != os.getpid():
                return True
    return False


def check_call_valid():
    word = 'if not validate(token):'
    with open(os.getcwd() + '/app/routes.py') as f:
        for l_num, l in enumerate(f, 1):
            if word in l:
                if '#' not in l.strip():
                    return True
        return False


def validate(token):
    if check_call_valid():
        if is_running("check_licence.py"):
            if is_valid(token):
                return True
    return False


def is_valid(token):
    return token == '7bdb3adea2e032b0e2e31116f48080a3'  # TODO mudar para consulta no banco


def not_valid():
    return {"success": False}, 401
