# RoohiAI/config.py

import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================================
# BOT INFO
# ==========================================================

BOT_NAME = os.getenv("BOT_NAME", "RoohiAI")
BOT_USERNAME = os.getenv("BOT_USERNAME", "RoohiAIBot")

# ==========================================================
# TELEGRAM
# ==========================================================

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

STRING_SESSION = os.getenv("STRING_SESSION", "")
STRING_SESSION2 = os.getenv("STRING_SESSION2", "")
STRING_SESSION3 = os.getenv("STRING_SESSION3", "")

# ==========================================================
# OWNERS
# ==========================================================

OWNER_ID = int(os.getenv("OWNER_ID", 0))

SUDO_USERS = list(
    map(
        int,
        filter(
            None,
            os.getenv("SUDO_USERS", "").split()
        )
    )
)

# ==========================================================
# DATABASE
# ==========================================================

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///roohi.db"
)

REDIS_URI = os.getenv("REDIS_URI", "")

# ==========================================================
# OPENROUTER
# ==========================================================

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY",
    ""
)

DEFAULT_AI_MODEL = os.getenv(
    "DEFAULT_AI_MODEL",
    "openrouter"
)

# ==========================================================
# OPENAI
# ==========================================================

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY",
    ""
)

# ==========================================================
# GROK
# ==========================================================

GROK_API_KEY = os.getenv(
    "GROK_API_KEY",
    ""
)

# ==========================================================
# QWEN
# ==========================================================

QWEN_API_KEY = os.getenv(
    "QWEN_API_KEY",
    ""
)

# ==========================================================
# LLAMA
# ==========================================================

LLAMA_API_KEY = os.getenv(
    "LLAMA_API_KEY",
    ""
)

# ==========================================================
# IMAGE GENERATION
# ==========================================================

POLLINATIONS_ENABLED = (
    os.getenv(
        "POLLINATIONS_ENABLED",
        "True"
    ).lower()
    == "true"
)

# ==========================================================
# MUSIC
# ==========================================================

AUTO_LEAVE = int(
    os.getenv(
        "AUTO_LEAVE",
        300
    )
)

MAX_QUEUE_SIZE = int(
    os.getenv(
        "MAX_QUEUE_SIZE",
        1000
    )
)

DEFAULT_VOLUME = int(
    os.getenv(
        "DEFAULT_VOLUME",
        100
    )
)

# ==========================================================
# VOICE ASSISTANT
# ==========================================================

WAKE_WORD = os.getenv(
    "WAKE_WORD",
    "roohi"
)

VOICE_LANGUAGE = os.getenv(
    "VOICE_LANGUAGE",
    "en"
)

ENABLE_VOICE_AI = (
    os.getenv(
        "ENABLE_VOICE_AI",
        "True"
    ).lower()
    == "true"
)

# ==========================================================
# QUIZ
# ==========================================================

QUIZ_TIME_LIMIT = int(
    os.getenv(
        "QUIZ_TIME_LIMIT",
        30
    )
)

QUIZ_REWARD_POINTS = int(
    os.getenv(
        "QUIZ_REWARD_POINTS",
        10
    )
)

# ==========================================================
# CACHE
# ==========================================================

CACHE_TIME = int(
    os.getenv(
        "CACHE_TIME",
        600
    )
)

# ==========================================================
# LOGGING
# ==========================================================

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)

# ==========================================================
# SECURITY
# ==========================================================

COMMAND_COOLDOWN = int(
    os.getenv(
        "COMMAND_COOLDOWN",
        3
    )
)

SPAM_LIMIT = int(
    os.getenv(
        "SPAM_LIMIT",
        5
    )
)

# ==========================================================
# PATHS
# ==========================================================

DOWNLOADS_DIR = "downloads"
CACHE_DIR = "cache"
TEMP_DIR = "temp"

# ==========================================================
# VERSION
# ==========================================================

VERSION = "1.0.0"