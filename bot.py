import os
import random
from dotenv import load_dotenv
from telegram import Update
from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import CallbackContext
from telegram.ext import Filters

load_dotenv()
BOT_API = os.environ.get("BOT_API")


class Event:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

    def __str__(self):
        return f"Название: {self.title}\nОписание:{self.description}"


EVENTS = [Event("Доктор", "Персонаж с наименьшим количеством хп восстаналвиет одну жизнь"),
          Event("Перестрелка", "Каждый игрок может использовать 2 бэнга, а не один")]


def new_event_button_handler(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="новое событие")]])
    random_event = random.choice(EVENTS)

    update.message.reply_text(text=str(random_event), reply_markup=reply_markup)


def main():
    updater = Updater(token=BOT_API, use_context=True)
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=new_event_button_handler))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
