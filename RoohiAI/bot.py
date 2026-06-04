# RoohiAI/bot.py

import asyncio
import sys

from pyrogram import Client, idle

from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    BOT_NAME,
)

from core.logger import logger
from core.loader import boot_plugins

# ==========================================================
# VALIDATION
# ==========================================================

REQUIRED_VARS = {
    "API_ID": API_ID,
    "API_HASH": API_HASH,
    "BOT_TOKEN": BOT_TOKEN,
}

missing = [
    key for key, value in REQUIRED_VARS.items()
    if not value
]

if missing:
    print(
        f"Missing environment variables: "
        f"{', '.join(missing)}"
    )
    sys.exit(1)

# ==========================================================
# MAIN BOT CLIENT
# ==========================================================

app = Client(
    name="RoohiAI",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=100,
    sleep_threshold=30,
)

# ==========================================================
# STARTUP
# ==========================================================

async def startup():

    logger.info("=" * 60)
    logger.info(f"{BOT_NAME} Starting...")
    logger.info("=" * 60)

    # Load all plugins
    boot_plugins()

    # Start bot
    await app.start()

    me = await app.get_me()

    logger.info(
        f"Bot Started Successfully "
        f"as @{me.username}"
    )

    logger.info(
        f"Name: {me.first_name}"
    )

    logger.info(
        f"ID: {me.id}"
    )

# ==========================================================
# SHUTDOWN
# ==========================================================

async def shutdown():

    logger.warning(
        "Stopping RoohiAI..."
    )

    try:
        await app.stop()
    except Exception as e:
        logger.error(
            f"Shutdown Error: {e}"
        )

# ==========================================================
# RUNNER
# ==========================================================

async def main():

    try:

        await startup()

        logger.info(
            "RoohiAI is now online."
        )

        await idle()

    except KeyboardInterrupt:

        logger.warning(
            "Keyboard Interrupt Received"
        )

    except Exception as e:

        logger.error(
            f"Fatal Error: {e}"
        )

    finally:

        await shutdown()

# ==========================================================
# ENTRY
# ==========================================================

if __name__ == "__main__":
    asyncio.run(main())