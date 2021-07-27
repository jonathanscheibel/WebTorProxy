def validate(token):
    return is_valid(token)


def is_valid(token):
    return token == '7bdb3adea2e032b0e2e31116f48080a3'


def not_valid():
    return {"success": False}, 401

