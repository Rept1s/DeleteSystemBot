# DeleteSystemBot

# Введение

### Описание бота:

### Телеграм бот который удаляет любые сообщения в группе, в том числе сообщения о входе и выходе пользовалетей из группы.


### Возможности:

- _Поддержка любых ссылок в кнопке в привественном сообщении._
  
- _Рассылка по всем пользователям бота._
  
- _Рассылка по всем группам, в которых добавлен бота._

- _Ежедневная автоматическая рассылка сообщения по всем группам._
  
- _Возможность выгрзуить количество пользователей в боте._

- _Возможность выгрузить айди и названий групп в которых добавлен бот._

- _Возможность добавить ссылку на правила/пользовательское соглашение с которым пользователю необходимо согласиться._

- _Удаляет сообщения пользователя в случае, если пользователь после согласия с правилами решил отписаться от каналов._

### Команды:

- _/list= (Посмотреть группы в которые добавлен бота)_

- _/users= (Посмотреть количество пользовалей в боте)_

- _/send_chat= (Произвести рассылку по всем группам с ботом)_

- _/send_user= (Произвести рассылку по всем пользователям бота)_


# Установка и настройка
## Версия:
### __❗ Используемая версия Python - 3.11.__

## Установка:

1. Клонировать данный репозиторий:

```git clone https://github.com/Rept1s/DeleteSystemBot```

2. Перейти в папку:

```cd DeleteSystemBot```

3. Установка требований:

```pip3 install -r requirements.txt```

## Настройка:__1. Создать бота в @BotFather и получить его токен.__

__2. Перейти в файл "input" и ввести необходимые данные:__

- _MSG_ID= (ID Сообщение для ежедневной рассылки)_
  
- _TIME_POST= (Время ежедневной рассылки (в часах)(МСК))_

- _TOKEN= (Токен бота, получить можно при создании бота в @BotFather)_

- _FROM_CHAT= (Чат из которого брать сообщение для ежедневной рассылки)_
  
- _ADM_ID= (ID Администраторов бота, можно несколько указывая через запятую без пробела)_

- _DB_PATCH= (Абсолютный путь к базе данных, заканчивается на "....../SystemDeleteBot/core/database.db")_

- _LINK_BOT_INVITE= (Ссылка кнопки, которое будет указано в приветственном сообщении, (startgroup) - приглашение в группу (начинать с t.me))_


# Запуск

## После настройки:

- _Необходимо добавить бота в группу и выдать права админстратора для корректной работы бота._

## Запуск бота

- ```run main.py```
  
- ```python3 main.py```
  
# Разработчик

__Разработано by Rept1s/developed by Rept1s.__
