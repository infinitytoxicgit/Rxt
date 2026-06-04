# RoohiAI/core/logger.py

import logging
import os
from logging.handlers import RotatingFileHandler

# ==========================================================
# CREATE LOG DIRECTORY
# ==========================================================

LOG_DIR = "logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# ==========================================================
# LOG FORMAT
# ==========================================================

LOG_FORMAT = (
    "[%(asctime)s] "
    "[%(levelname)s] "
    "[%(name)s] "
    "%(message)s"
)

DATE_FORMAT = "%d-%b-%Y %H:%M:%S"

formatter = logging.Formatter(
    LOG_FORMAT,
    datefmt=DATE_FORMAT
)

# ==========================================================
# ROOT LOGGER
# ==========================================================

logger = logging.getLogger("RoohiAI")
logger.setLevel(logging.INFO)

# ==========================================================
# CONSOLE HANDLER
# ==========================================================

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# ==========================================================
# FILE HANDLER
# ==========================================================

file_handler = RotatingFileHandler(
    filename="logs/roohi.log",
    maxBytes=10 * 1024 * 1024,  # 10MB
    backupCount=5,
    encoding="utf-8"
)

file_handler.setFormatter(formatter)

# ==========================================================
# ERROR FILE HANDLER
# ==========================================================

error_handler = RotatingFileHandler(
    filename="logs/errors.log",
    maxBytes=10 * 1024 * 1024,
    backupCount=5,
    encoding="utf-8"
)

error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

# ==========================================================
# ATTACH HANDLERS
# ==========================================================

if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addHandler(error_handler)

# ==========================================================
# PYROGRAM LOGS
# ==========================================================

logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pytgcalls").setLevel(logging.WARNING)
logging.getLogger("aiohttp").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)

# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def info(message: str):
    logger.info(message)

def warning(message: str):
    logger.warning(message)

def error(message: str):
    logger.error(message)

def critical(message: str):
    logger.critical(message)

def debug(message: str):
    logger.debug(message)

# ==========================================================
# STARTUP LOG
# ==========================================================

logger.info("RoohiAI Logger Initialized")