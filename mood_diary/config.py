from pathlib import Path


# Все настройки в одном месте!
MOOD_FILE_PATH = "data/entries.txt"
BASE_DIR = Path(__file__).parent.parent
MOOD_FILE = BASE_DIR / MOOD_FILE_PATH
VALID_MOODS = ('good', 'bad', 'neutral', 'excellent')

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
ENCODING = "utf-8"
MAX_ENTRIES = 1000