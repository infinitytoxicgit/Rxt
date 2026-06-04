# RoohiAI/core/loader.py

import importlib
from pathlib import Path

from core.logger import logger

# ==========================================================
# PLUGIN ROOT
# ==========================================================

PLUGIN_DIR = Path("plugins")

# ==========================================================
# IGNORED FILES
# ==========================================================

IGNORE = {
    "__init__.py",
    "__pycache__"
}

# ==========================================================
# STATS
# ==========================================================

LOADED_PLUGINS = []
FAILED_PLUGINS = []

# ==========================================================
# IMPORT SINGLE MODULE
# ==========================================================

def load_plugin(module_path: str):
    try:
        importlib.import_module(module_path)

        LOADED_PLUGINS.append(module_path)

        logger.info(
            f"[PLUGIN LOADED] {module_path}"
        )

        return True

    except Exception as e:

        FAILED_PLUGINS.append(
            {
                "plugin": module_path,
                "error": str(e)
            }
        )

        logger.error(
            f"[PLUGIN FAILED] {module_path} | {e}"
        )

        return False

# ==========================================================
# LOAD ALL PLUGINS
# ==========================================================

def load_plugins():

    logger.info(
        "Searching plugins..."
    )

    if not PLUGIN_DIR.exists():

        logger.warning(
            "plugins directory not found."
        )

        return

    for category in PLUGIN_DIR.iterdir():

        if not category.is_dir():
            continue

        category_name = category.name

        for file in category.glob("*.py"):

            if file.name in IGNORE:
                continue

            plugin_name = file.stem

            module_path = (
                f"plugins."
                f"{category_name}."
                f"{plugin_name}"
            )

            load_plugin(module_path)

# ==========================================================
# REPORT
# ==========================================================

def plugin_report():

    logger.info(
        "=" * 50
    )

    logger.info(
        f"Loaded: {len(LOADED_PLUGINS)}"
    )

    logger.info(
        f"Failed: {len(FAILED_PLUGINS)}"
    )

    if FAILED_PLUGINS:

        logger.warning(
            "Failed Plugin List:"
        )

        for plugin in FAILED_PLUGINS:

            logger.warning(
                f"{plugin['plugin']} "
                f"-> {plugin['error']}"
            )

    logger.info(
        "=" * 50
    )

# ==========================================================
# BOOT
# ==========================================================

def boot_plugins():

    logger.info(
        "Starting Plugin Loader..."
    )

    load_plugins()

    plugin_report()

    logger.info(
        "Plugin Loader Finished."
    )