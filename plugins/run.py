from pyrogram import Client , Message , Filters
from db import r
import os , time



@Client.on_message(Filters.me & Filters.regex("^[Pp]y$") & Filters.reply , group=13)
def runpy(app : Client , msg : Message):

    text = msg.reply_to_message.text
    with open("script.py", "a+") as f_w:
        f_w.write(text)
    os.system("python3 script.py > out.txt")
    with open("out.txt", "r") as f_r:
        out = f_r.read()
        out = "Output:\n" + out
    os.remove("script.py")
    os.remove("out.txt")
    app.edit_message_text(msg.chat.id,msg.message_id,out)
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)