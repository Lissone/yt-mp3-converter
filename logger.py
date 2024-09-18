import os
from datetime import datetime
import logging

# ----------------------------------------------- #

LOG_DIR = 'logs'
LOG_FILE = os.path.join(LOG_DIR, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

# ----------------------

ANSI_COLORS = {
    'reset': '\033[0m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m'
}

# ----------------------------------------------- #

def setup_logger():
    """Configure the logger to save logs to file and display on the console with colors."""
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger('yt-dlp')
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    class ColorFormatter(logging.Formatter):
        def format(self, record):
            if record.levelno == logging.WARNING:
                record.msg = f"{ANSI_COLORS['yellow']}{record.msg}{ANSI_COLORS['reset']}"
            elif record.levelno == logging.ERROR:
                record.msg = f"{ANSI_COLORS['red']}{record.msg}{ANSI_COLORS['reset']}"
            elif record.levelno == logging.INFO:
                record.msg = f"{ANSI_COLORS['green']}{record.msg}{ANSI_COLORS['reset']}"
            elif record.levelno == logging.DEBUG:
                record.msg = f"{ANSI_COLORS['blue']}{record.msg}{ANSI_COLORS['reset']}"
            return super().format(record)

    console_handler.setFormatter(ColorFormatter('%(levelname)-8s %(message)s'))

    file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
