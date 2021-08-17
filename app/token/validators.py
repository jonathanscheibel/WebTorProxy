from app import db


def validate(token):
    if is_into_limit():
        return is_valid(token)
    return False


def is_into_limit():
    LIMIT_LICENCE = 1000
    return int(db.select('SELECT count(token) from change')[0]) <= LIMIT_LICENCE


def is_valid(token):
    return token == '7bdb3adea2e032b0e2e31116f48080a3' # TODO mudar para consulta no banco


def not_valid():
    return {"success": False}, 401

