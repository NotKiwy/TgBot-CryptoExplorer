import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()
support = os.getenv("SUPPORT")
community = os.getenv("COMMUNITY")

wkb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Выбрать крипто-валюту 🚀", callback_data="_crypto_")
        ],
        [
            InlineKeyboardButton(text="Поддержка 🛠", url=support),
            InlineKeyboardButton(text="Комьюнити 🤝", url=community)
        ]
    ]
)