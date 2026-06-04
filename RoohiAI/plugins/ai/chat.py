# RoohiAI/plugins/ai/chat.py

from pyrogram import filters

from core.client import app

from keyboards.home import (
    home_keyboard
)

@app.on_message(
    filters.command("start")
)
async def start_command(
    client,
    message
):

    await message.reply_text(
        text=(
            "👋 Welcome to RoohiAI\n\n"
            "AI Assistant Online."
        ),
        reply_markup=home_keyboard()
    )