from pathlib import Path
import logging
import os

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]  # change here!
USE_TOR_SOCKS = True  # change here
FILES_FOLDER = Path('.') / 'files'
if not FILES_FOLDER.exists():
    FILES_FOLDER.mkdir()

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
)
