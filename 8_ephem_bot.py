"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

import settings1

PROXY = {
  'proxy_url': settings1.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings1.PROXY_USERNAME,
        'password': settings1.PROXY_PASSWORD
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def planet_list(planet):
  planet = update.message.text


def planet_place_answer(update, context):
       
    update.message.reply_text(planet_position(planet))


def main():
    mybot = Updater(settings1.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

import ephem

mars = ephem.Mars('2000/01/01')
constellation = ephem.constellation(mars)
print(constellation)


if __name__ == "__main__":
    main()
