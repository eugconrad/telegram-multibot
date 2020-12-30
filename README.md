### Простой русскоговорящий selfbot для Телеграма
<p >
    <a href="">
        <img src="https://raw.githubusercontent.com/Conradk10/telegram-multibot/pics/multibotby.jpg" alt="Multibot">
    </a>
	<br>
	</br>

### О проекте
Multibot разработан для личного аккуанта Телеграм. Не для ботов (!)
 - Multibot представляет из себя модульного бота с набором различных развлекательно-инфррмационных чат-функций а так же автоматизацию неких задач, таких как автоответчик и тд
 - Бот легко может дополняться с помощью написания подключаемых плагинов на языке Python


Контакты:
</p>
<p >
	<a href="https://t.me/zxvghost666">
        <img src="https://icons.iconarchive.com/icons/froyoshark/enkel/512/Telegram-icon.png" alt="Разработчик" height="75" width="75">
    </a>
</p>

### Требования
- Python версии 3.6 или новее
- Telegram API ключ (https://my.telegram.org/apps)

### Библиотеки (Всё есть в requirements.txt)
<a href=https://github.com/pyrogram/pyrogram>pyrogram</a><br>
<a href=https://github.com/paramiko/paramiko>paramiko</a><br>
<a href=https://github.com/giampaolo/psutil>psutil</a><br>
<a href=https://github.com/andymccurdy/redis-py>redis</a><br>
<a href=https://github.com/psf/requests>requests</a>

### Установка
1 - Получение API ID и ключа
  - Для начала нужно перейти по <a href=https://my.telegram.org/auth>ссылке</a>
  - Ввести номер телефона и нажать `API development tools`
  - Держать рядом `App api_id` и `App api_hash`

2 - Сама установка
```bash
git clone https://github.com/Conradk10/telegram-multibot
cd telegram-multibot/
```
3 - Подготовка бота
  - В файл config.ini вставить `api_id` и `api_hash`


***ВНИМАНИЕ: Если вы будете использовать API_KEY чужого аккаунта, то ВАШ аккаунт будет удален Телеграмом!***

4 - Подготовка базы данных
```bash

***База данных***
#Debian
sudo apt install redis-server
#Arch
sudo pacman -S redis-server
#Fedora
sudo dnf -y install redis
#Включить и запустить базу данных
service redis-server enable
service redis-server start


*** Подготовка к запуску и сам запуск ***
pip3 install -r requirements.txt
python3 bot.py
```


### Список команд
  - `help` - это сообщение
  - `about` - о боте
  - `settings` - настройки
  - `boss` - доверенный аккаунт
  - `autodel` - отключить автоудаление сообщений
  - `autodel` (сек) - время автоудаления сообщений

  - `server `- инфо сервера
  - `connect` - подключиться по ssh к серверу
  - `exit()` - отключиться по shh от сервера

  - `today` - текущие дата и время
  - `id` - узнать id юзера (через ответ)

  - `spam` (кол-во) - спам (через ответ)
  - `spamf` (кол-во) - спам фразами
  - `addf` - добавить фразу для спама
  - `delf` - удалить фразу для спама
  - `listf` - список фраз для спама
  - `clearf` - оичстить список фраз

  - `action` - вкл/выкл чат действие
  - `setaction` (действие) - установить чат действие
  - `actionlist` - список доступных чат действий

  - `set (команда)` - установить быструю команду на вложение (через ответ)
  - `cmdlist` - список доступных быстрых команд
  - `dcmd (команда)` - удалить быструю команду

  - `nobody` - никто не видит статус онлайна
  - `everybody` - все видят статус онлайна
  - `mark` - добавить чат в отмеченные
  - `marklist` - список отмеченных чатов
  - `m` - заглушить
  - `offline` - вкл/выкл режим **Не беспокоить**

  - `d` - удалить сообщение (через ответ)
  - `b` - заблокировать юзера (через ответ)
  - `ub` - разблокировать юзера (через ответ)
  - `pin` - закрепить сообщение (через ответ)
  - `unpin` - открепить сообщение (через ответ)
  - `kick` - кикнуть юзера (через ответ)

### Планы на будущее
 - Оптимизировать код
 - Сделать код более гибким и универсальным
 - Добавить больше плагинов (каких? пока секрет)
 - Добавить плагин: отсчет до указанной пользователем даты, уведомление о наступившей дате
 - Список будет дополняться...
