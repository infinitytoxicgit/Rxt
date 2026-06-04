# RoohiAI/keyboards/home.py

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

def home_keyboard():

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🤖 AI",
                    callback_data="home_ai"
                ),
                InlineKeyboardButton(
                    "🎵 Music",
                    callback_data="home_music"
                )
            ],
            [
                InlineKeyboardButton(
                    "🧠 Quiz",
                    callback_data="home_quiz"
                ),
                InlineKeyboardButton(
                    "💻 Coding",
                    callback_data="home_coding"
                )
            ],
            [
                InlineKeyboardButton(
                    "⚙ Settings",
                    callback_data="home_settings"
                )
            ]
        ]
    )