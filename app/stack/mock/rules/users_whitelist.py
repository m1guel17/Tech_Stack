import os

def whitelist() -> bool | list:
    if os.getenv("whitelist") is None:
        return False
    else:
        return os.getenv("whitelist").split(",")

whitelist()