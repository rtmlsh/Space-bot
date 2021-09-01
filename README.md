# Загрузка фотографий космоса в Telegram 
Скрипт интегрируется с API [NASA](https://api.nasa.gov/) и [SpaceX](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1), скачивает фотографии и публикует их на канал в Телеграме с помощью библиотеки [Python Telegram Bot](https://python-telegram-bot.readthedocs.io/en/stable/). 

## Как установить  
На компьютере должен быть уже установлен Python3. Для запуска скрипта установите виртуальное окружение: 
> python3 -m venv venv

Затем активируйте виртуальное окружение (вариант для Windows):
> venv\Scripts\activate 

Затем активируйте виртуальное окружение (вариант для Mac OS):
> source venv/bin/activate

Используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей: 
> pip install -r requirements.txt 

Скрипт работает с переменными окружения для взаимодействия с API [NASA](https://api.nasa.gov/) и каналом в Телеграме. Для успешной работы скрипта необходимо получить токены API NASA, телеграм-бота и chat-id телеграм-канала, записать их в .env файл: 
> echo NASA_TOKEN=токен > .env 

> echo TELEGRAM_TOKEN=токен > .env 

> echo CHAT_ID=chat-id > .env

Запуск скрипта осуществляется в командной строке: 
> python main.py

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [Devman](https://dvmn.org/modules/). 
