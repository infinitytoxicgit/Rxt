# RoohiAI/bot.py

import asyncio

from pyrogram import idle

from core.client import app

from core.loader import (
    boot_plugins
)

from core.logger import logger


async def main():

    boot_plugins()

    await app.start()

    me = await app.get_me()

    logger.info(
        f"Started as @{me.username}"
    )

    await idle()

    await app.stop()


if __name__ == "__main__":
    asyncio.run(main())