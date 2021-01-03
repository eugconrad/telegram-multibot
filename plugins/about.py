from pyrogram import Client , Message , Filters
from db import r
import bot
import time

abouttext = bot.botfullprefix + """О проекте:

`Multibot` представляет из себя русскоговорящего модульного юзербота с набором различных развлекательно-инфррмационных функций а так же автоматизацию неких задач, таких как автоответчик и тд
Бот легко может дополняться с помощью написания пользовательских плагинов на языке Python

`Multibot` разработан для личного аккаунта Telegram (userbot). Не для использования в ботах (!)

""" + bot.botfullsuffix

@Client.on_message(Filters.regex("!about") & Filters.me, group=0)
def help(app : Client ,msg : Message):
    app.delete_messages(msg.chat.id, msg.message_id)
    app.send_photo(
        msg.chat.id,
        "https://raw.githubusercontent.com/Conradk10/telegram-multibot/pics/multibotby.jpg",
        caption=abouttext
        )

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
