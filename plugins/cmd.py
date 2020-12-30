from pyrogram import Client , Message , Filters
from db import r
import time



### SET A FILE AS CMD
@Client.on_message(Filters.me  & Filters.reply & Filters.regex("^[Ss]et (.*)$") , group=0)
def setcmd(app : Client ,msg : Message):
    cmd = msg.text.split(" ")[1]
    rmsg = msg.reply_to_message
    if rmsg.sticker:
        fid = "STICKER:"+str(rmsg.sticker.file_id)
        r.hmset("qanswer", {cmd: fid})
    elif rmsg.animation:
        fid = "GIF:"+str(rmsg.animation.file_id)
        r.hmset("qanswer", {cmd: fid})
    elif rmsg.photo:
        fid = "PHOTO:"+str(rmsg.photo.sizes[-1].file_id)
        r.hmset("qanswer", {cmd: fid})
    elif rmsg.video:

        fid = "VIDEO:"+str(rmsg.video.file_id)
        r.hmset("qanswer", {cmd: fid})
    elif rmsg.document:

        fid = "DOC:"+str(rmsg.document.file_id)
        r.hmset("qanswer", {cmd: fid})
    elif  rmsg.video_note:
        fid = "VN:"+str(rmsg.video_note.file_id)
        r.hmset("qanswer", {cmd: fid})
    elif rmsg.voice:
        fid = "VOICE:"+str(rmsg.voice.file_id)
        r.hmset("qanswer", {cmd: fid})
    elif rmsg.audio:
        fid = "MUSIC:"+str(rmsg.audio.file_id)
        print(fid)
        r.hmset("qanswer", {cmd: fid})

    else:return
    app.edit_message_text(msg.chat.id,msg.message_id,f"**[Multibot]** Быстрая команда `{cmd}` на это вложение успешно установлена")
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)


### SHOW CMD LIST
@Client.on_message(Filters.regex("^[Cc]mdlist$") & Filters.me , group=1)
def cmdlist(app : Client ,msg : Message):
    text = "**[Multibot]** Список доступых быстрых команд:\n"
    cmds = r.hgetall("qanswer")
    for i in cmds:
        text = text + f"`{i}` - __{cmds[i].split(':')[0]}__\n"

    app.edit_message_text(msg.chat.id,msg.message_id,text)
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)

### DEL CMD
@Client.on_message(Filters.regex("^[Dd]cmd (.*)$") & Filters.me , group=2)
def delcmd(app : Client ,msg : Message):
    cmd = msg.text.split(" ")[1]
    r.hdel("qanswer", cmd)
    app.edit_message_text(msg.chat.id,msg.message_id,f"**[Multibot]** Быстрая команда `{cmd}` успешно удалена")
    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)


@Client.on_message(Filters.text & Filters.me, group=3)
def cmd (app : Client , msg : Message):
    text = msg.text
    if text in r.hgetall("qanswer"):
        txt = r.hgetall("qanswer")[text]
        t = txt.split(":")
        msg_id = None
        if msg.reply_to_message: msg_id = msg.reply_to_message.message_id
        if t[0] == "GIF":
            #sendgif
            app.send_animation(msg.chat.id,t[1],reply_to_message_id=msg_id)
        elif t[0] == "STICKER":
            app.send_sticker(msg.chat.id, t[1], reply_to_message_id=msg_id)

        elif t[0] == "VN":
            app.send_video_note(msg.chat.id, t[1], reply_to_message_id=msg_id)

        elif t[0] == "VOICE":
            app.send_voice(msg.chat.id, t[1], reply_to_message_id=msg_id)

        elif t[0] == "VIDEO":
            app.send_video(msg.chat.id, t[1], reply_to_message_id=msg_id)

        elif t[0] == "DOC":
            app.send_document(msg.chat.id, t[1], reply_to_message_id=msg_id)

        elif t[0] == "PHOTO":
            app.send_photo(msg.chat.id, t[1], reply_to_message_id=msg_id)

        app.delete_messages(msg.chat.id, msg.message_id)
    else:return
