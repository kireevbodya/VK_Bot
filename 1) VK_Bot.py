# -*- coding: utf-8 -*-

import pyowm
# Библиотека pyowm отвечает за погоду.

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
# Библиотека vk_api отвечает за управление ботом.

import _datetime
import datetime
# Библиотека _datetime, datetime дает возможность получить дату и время.

from pycbrf.toolbox import ExchangeRates
# Библиотека pycbrf выполняет запрос на офицальный сайт ЦБ и выдёт значение валюты.

import time
# Используем библиотеку time, что бы сделать маленькую задержку перед отправкой сообщения ботом.
# Иногда ВК считает сообщения бота, как спам, поэтому задержка обязательно должна быть.

from random import choice
# Библиотека random отвечает за систему случайного выбора.


# Функция для отправки сообщений пользователю.
def write_message(user_id, random_id, message):
    vk.method("messages.send", {"user_id": user_id, "random_id": random_id, "message": message})


# Функция для получения данных о погоде.
def weather(city):
    # API-token для библиотеки pyown.
    weather_token = pyowm.OWM("79bb6125d9f25982bc53f52dd60a7e59")

    observation = weather_token.weather_at_place(city)
    weather = observation.get_weather()
    temperature = weather.get_temperature("celsius")["temp"]

    write_message(event.user_id, event.random_id, "В городе " + city + " сейчас температура: "
                  + str(int(temperature)) + " по Цельсию.")


# Функция для получения данных о стоимости валюты.
def currency(name):
    date = _datetime.date.today()

    rates = ExchangeRates(date)
    value = rates[name].value

    write_message(event.user_id, event.random_id, "Значение " + name + " на сегодняшний "
                                                                       "день равен: " + str(value))


# Функция для получения точной даты и времени.
def date_time():
    now = datetime.datetime.now()

    h = str(now.hour)
    min = str(now.minute)
    s = str(now.second)

    d = str(now.day)
    m = str(now.month)
    y = str(now.year)

    write_message(event.user_id, event.random_id, "Дата: " + d + "." + m + "." + y)
    time.sleep(0.5)

    write_message(event.user_id, event.random_id, "Время по МСК: " + h + "ч" + " - " + min + "м" + " - "
                  + s + "с")


# Функция для игры в Magic Ball.
def magic_ball():
    answers = ['Бесспорно.', 'Предрешено.', 'Никаких сомнений.', 'Определённо да.',
               'Можешь быть уверен в этом.', 'Мне кажется — «да».', 'Вероятнее всего.',
               'Хорошие перспективы.', 'Знаки говорят — «да».', 'Да.',
               'Пока не ясно, попробуй снова.', 'Спроси позже.', 'Лучше не рассказывать.',
               'Сейчас нельзя предсказать.', 'Сконцентрируйся и спроси опять.',
               'Даже не думай.', 'Мой ответ — «нет».', 'По моим данным — «нет».',
               'Перспективы не очень хорошие.', 'Весьма сомнительно.']

    write_message(event.user_id, event.random_id, "Сыграем в игру.")
    time.sleep(1)

    write_message(event.user_id, event.random_id, "Подумай, что ты хочешь сделать, "
                  + "а я напишу стоит ли так поступать.")
    time.sleep(8)

    write_message(event.user_id, event.random_id, "Подумал?")
    time.sleep(3)

    write_message(event.user_id, event.random_id, "Мой ответ:")
    time.sleep(1)

    write_message(event.user_id, event.random_id, choice(answers))


# API-token для управления ботом.
token = "9c71f98d249152fb8c5ac28896b08675b1c0266033f6c54d82a8fc0f5e5c0c8e60db4838b2c303185eeea"


# Авторизуемся как сообщество.
vk = vk_api.VkApi(token=token)


# Работа с сообщениями.
longpoll = VkLongPoll(vk)


# Список с командами.
commands = ["/help", "/whatcanbotdo", "/weather", "/currency", "/date_time", "/magic_ball"]


# Список с приветсвиями.
greetings1 = ["Привет.", "привет.", "Привет!", "привет!", "Привет", "привет",
             "Хай.", "хай.", "Хай!", "хай!", "Хай", "хай"]

greetings2 = ["Как дела?", "как дела?", "Как дела", "как дела"]

# Основновная программа.
for event in longpoll.listen():

    # Если пришло новое сообщение.
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для бота.
        if event.to_me:

            # Сообщение от пользователя.
            request = event.text

            # Варианты ответов на команды пользователя.
            if request[0] == "/" and request not in commands:
                write_message(event.user_id, event.random_id, "Неизвестная команда.")

            elif request in greetings1:
                write_message(event.user_id, event.random_id, "Здравствуйте!!!")

            elif request in greetings2:
                write_message(event.user_id, event.random_id, "У меня все хорошо :)")

            elif request == "Начать" or request == "Старт":
                write_message(event.user_id, event.random_id, "Привет, я Бот Ботович. Рад знакомству.")
                time.sleep(1)

                write_message(event.user_id, event.random_id, "Я запрограммирован для помощи людям.")
                time.sleep(1)

                write_message(event.user_id, event.random_id, "Чтобы узнать о моих возможностях используй команду:")
                time.sleep(1)

                write_message(event.user_id, event.random_id, "/whatcanbotdo")
                time.sleep(1)

                write_message(event.user_id, event.random_id, "Чтобы ознакомиться со списком всех "
                                                              "моих команд используй:")

                time.sleep(1)

                write_message(event.user_id, event.random_id, "/help")

            elif request == "/help":
                write_message(event.user_id, event.random_id, "Список моих комманд:")
                time.sleep(1)

                write_message(event.user_id, event.random_id, "/whatcanbotdo, /help")
                time.sleep(0.5)

                write_message(event.user_id, event.random_id, "/weather, /currency, /date_time")
                time.sleep(0.5)

                write_message(event.user_id, event.random_id, "/magic_ball")

            elif request == "/whatcanbotdo":
                write_message(event.user_id, event.random_id, "Данный бот умеет:")
                time.sleep(1)

                write_message(event.user_id, event.random_id, "Выдавать температуру воздуха в Пензе, Москве и СПб.")
                time.sleep(1)

                write_message(event.user_id, event.random_id, "/weather")
                time.sleep(1)

                write_message(event.user_id, event.random_id, "Выдавать значение Доллара и Евро на сегодняшний день.")
                time.sleep(1)

                write_message(event.user_id, event.random_id, "/currency")
                time.sleep(1)

                write_message(event.user_id, event.random_id, "Выдавать точную дату и время.")
                time.sleep(1)

                write_message(event.user_id, event.random_id, "/date_time")
                time.sleep(1)

                write_message(event.user_id, event.random_id, "Так-же в боте реализована функция магического шара.")
                time.sleep(1)

                write_message(event.user_id, event.random_id, "/magic_ball")

            elif request == "/weather":
                weather("Пенза")
                time.sleep(0.5)

                weather("Москва")
                time.sleep(0.5)

                weather("Санкт-Петербург")

            elif request == "/currency":
                currency("USD")
                time.sleep(0.5)

                currency("EUR")

            elif request == "/date_time":
                date_time()

            elif request == "/magic_ball":
                magic_ball()

            else:
                write_message(event.user_id, event.random_id, "Я вас не понял.")
