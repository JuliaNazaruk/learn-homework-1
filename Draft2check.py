import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

import settings

PROXY = {
  'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}

"""
Пишем приветственное сообщение пользователю и вызываем меню из планет
"""
import telebot

def greet_user(update, context):
    text = 'Привет! Этот бот умеет определять положение планеты на текущую дату. Выбери планету, положение которой хочешь узнать'
    print(text)
    update.message.reply_text(text)
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup_row ("Mercury", "Venus")
    user_markup_row ("Earth", "Mars")
    bot.send_message(message.from_user.id, reply_markup=user_markup)



def planet_list(planet):
  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
  user_markup_row ("Mercury", "Venus")
  user_markup_row ("Earth", "Mars")
  bot.send_message(message.from_user.id, reply_markup=user_markup)

"""
Импортируем модуль ephem, импортируем модуль с определением даты и времени
Определяем текущую дату
Определяем положение пданеты на текущую дату
"""


import ephem

from datetime import datetime
current_date = datetime.now().date()

def planet_place_answer(selected_planet):
    if message.text == "Mercury":
        position = ephem.Mercury(current_date)
        constellation = ephem.constellation(position)
        update.message.reply_text(constellation)

 


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, planet_place_answer))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()

#почему ephem и telebot выделены белым, а не ярко-зеленым, как Settings или logging
#почему без кусочка с if __name___ (2 посл строки ничего не работало, а после начал работать кусочек greet_user)