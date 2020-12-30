from pyrogram import Client , Message , Filters
from pyrogram.api import functions , types
from db import r
import time

### RECENTLY & ONLINE
@Client.on_message(Filters.me & Filters.regex("^([Nn]obody|[Ee]verybody)$") , group=0)
def setprivacy(app : Client ,msg : Message):
    if  "obody" in str(msg.text):
        app.send(
            functions.account.SetPrivacy(
                key=types.InputPrivacyKeyStatusTimestamp(),
                rules=[types.InputPrivacyValueDisallowAll()]
            )
        )
        app.edit_message_text(text="**[Multibot]** Режим невидимки `Вкл`",
            chat_id=msg.chat.id,
            message_id=msg.message_id,)
        r.set("lastseen", "NoBody")
        if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)


    else:
        app.send(
            functions.account.SetPrivacy(
                key=types.InputPrivacyKeyStatusTimestamp(),
                rules=[types.InputPrivacyValueAllowAll()]
            )
        )

        app.edit_message_text(text="**[Multibot]** Режим невидимки `Выкл`",
            chat_id=msg.chat.id,
            message_id=msg.message_id,)
        r.set("lastseen", "EveryBody")
        if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
