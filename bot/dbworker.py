from vedis import Vedis
from bot import config


# Пытаемься узнать из базы "состояние" пользователя
def get_state(key):
    with Vedis(config.DB_FILE) as db:
        try:
            return int(db[key].decode())
        except KeyError:
            return config.States.START.value


# Сохраняем текущее "состояние" пользователя в нашу базу
def set_state(key, value):
    with Vedis(config.DB_FILE) as db:
        try:
            db[key] = value
        except:
            False
