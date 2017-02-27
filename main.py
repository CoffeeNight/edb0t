#!/usr/bin/python3
import os
import logging

from telegram.ext import Updater

from bot.handlers import Handlers


KEY = os.environ.get('BOT_KEY', 'Please insert the real Key as an environment '
                                'variable BOT_KEY')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def start_bot():
    updater = Updater(KEY)
    dispatcher = updater.dispatcher
    handlers = Handlers(dispatcher)
    handlers.init_handlers()
    updater.start_polling()

if __name__ == '__main__':
    start_bot()
