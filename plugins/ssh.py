from pyrogram import Client , Message , Filters
from db import r
import time
import paramiko

isshhconnect = False
sshc = None

class ssh():
    def __init__(self, ip, username, password, port):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = int(port)
        self.isconnect = False

    def connectto(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(self.ip, username=self.username, password=self.password, port=self.port)
            self.isconnect = True
            self.ssh = ssh
            return "[SSH] Подключено"
        except:
            return "[SSH] Ошибка подключения"

    def cmd(self, tcmd):
        if self.isconnect == True:
            (stdin, stdout, stderr) = self.ssh.exec_command(tcmd)
            return stdin, stdout , stderr
        else:
            return False

    def disconnect(self):
        self.ssh.close()
        self.isconnect = False
        return "[SSH] Отключено"


### ADD SERVER FOR SSH
@Client.on_message(Filters.regex("^[Aa]ddserver$") & Filters.me & Filters.reply, group=38)
def addserver(app : Client ,msg : Message):
    text = msg.reply_to_message.text
    try:
        uname , elsee= text.split("@")
        ip, password = elsee.split(";")
        r.hmset("ssh", {"ip":ip, "username":uname , "password":password, "port":"22"})
        txt = f"USERNAME: {uname}\nPASSWORD: {password}\nPORT: 22\nIP: {ip}"
    except ValueError:
        txt = f"**wrong Format!**\nEx: root@192.168.21.1;psw123"
    app.edit_message_text(msg.chat.id,msg.message_id,txt)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)


### CONNECT TO SSH
@Client.on_message(Filters.regex("^[Cc]onnect$") & Filters.me , group=39)
def connecttossh(app : Client, msg : Message):
    global sshc, isshhconnect
    server = r.hgetall("ssh")
    ip = server["ip"]
    username = server["username"]
    password = server["password"]
    port = server["port"]
    sshconnect = ssh(ip, username, password, port)
    log = sshconnect.connectto()
    if log == "[SSH] Подключено":
        isshhconnect = True
        sshc = sshconnect
    else:
        pass
    app.edit_message_text(msg.chat.id,msg.message_id,log)

    if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)

@Client.on_message(Filters.text & Filters.me, group=-1)
def cmd_ssh(app : Client ,msg : Message):

    global sshc, isshhconnect
    text = msg.text
    if isshhconnect:
        if text == "exit()":
            isshhconnect = False
            sshc = None
            txt = "[SSH] Отключено"
        else:
            a, b, c = sshc.cmd(text)
            txt = b.read()
            txt = txt.decode("utf-8")
            txt = "[SSH] Ответ:\n" + txt

        app.edit_message_text(msg.chat.id,msg.message_id,txt)

        if r.get("autodel") == "on":
            time.sleep(float(r.get("autodeltime")))
            app.delete_messages(msg.chat.id,msg.message_id)
