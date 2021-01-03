import redis
import configparser
from db import r
from pyrogram import Client , errors
from pyrogram.errors import RPCError

# Read Config File
config = configparser.ConfigParser()
config.read("config.ini")
c = config["Config"]

# Настройка префикса сообщений бота
botprefix = "\ud83e\udd16 `Multibot` "
botversion = "`b0.4` "
botfullprefix = botprefix + botversion + "\n - "

# Настройка суффикса сообщений бота
botsuffix = "Ссылка на github проекта: "
botgithub = "https://github.com/Conradk10/telegram-multibot"
botfullsuffix = botsuffix + botgithub


def main():
    plugins = dict(root="plugins")
    API_ID = int(c["API_ID"])
    API_HASH = c["API_HASH"]

    Client(session_name="Multibot", api_id=API_ID, api_hash=API_HASH , plugins=plugins).run()
    if not r.get("autodeltime"): r.set("autodeltime", "10")


if __name__ == "__main__":
    main()
