from pyrogram import Client , Message , Filters
from db import r
import time , psutil
import bot

### DETAIL SERVER
@Client.on_message(Filters.me & Filters.regex("!server$"))
def server(app : Client ,msg : Message):

    cpu_f = dict(psutil.cpu_freq()._asdict())["current"]
    cpu_p = psutil.cpu_percent()
    disk_t = dict(psutil.disk_usage('/')._asdict())["total"]
    disk_u = dict(psutil.disk_usage('/')._asdict())["used"]
    disk_p = dict(psutil.disk_usage('/')._asdict())["percent"]
    ram_t = int(dict(psutil.virtual_memory()._asdict())["total"])
    ram_u = int(dict(psutil.virtual_memory()._asdict())["used"])
    ram_p = int(dict(psutil.virtual_memory()._asdict())["percent"])
    swap_t = int(dict(psutil.swap_memory()._asdict())["total"])
    swap_u = int(dict(psutil.swap_memory()._asdict())["used"])
    swap_p = int(dict(psutil.swap_memory()._asdict())["percent"])

    text = bot.botfullprefix + f"""Серверная информация:
ЦПУ загружен на `{cpu_p}%`
Частота ЦПУ `{cpu_f}` МГц
ОЗУ занято: `{int(ram_u/1048576)}` из `{int(ram_t/1048576)}` МБ - `{ram_p}%`
Swap занято: `{int(swap_u/1048576)}` из `{int(swap_t/1048576)}` МБ - `{swap_p}%`
Диск занято: `{int(disk_u/1048576)}` из `{int(disk_t/1048576)}` МБ - `{disk_p}%`
"""
    app.edit_message_text(text=text,
        chat_id=msg.chat.id,
        message_id=msg.message_id,)
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
