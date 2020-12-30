from pyrogram import Client , Message , Filters
from db import r
import time

abouttext = """
**[Multibot]** О проекте:

`Multibot` разработан для личного аккуанта Телеграм. Не для ботов (!)
`Multibot` представляет из себя модульного бота с набором различных развлекательно-ифонрмационных чат-функций а так же автоматизацию неких задач, таких как автоответчик и тд
Бот легко может дополняться с помощью написания подключаемых плагинов на языке Python

Ссылка на github проекта: https://github.com/Conradk10/telegram-multibot
"""

@Client.on_message(Filters.regex("^[Aa]bout$") & Filters.me, group=100)
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
