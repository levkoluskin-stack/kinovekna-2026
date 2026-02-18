"""
Конфигурация Киновекна 2026
"""

# ---- RSS-источники новостей ----
RSS_FEEDS = [
    # Русскоязычные
    {"url": "https://www.kinopoisk.ru/news.rss", "name": "Кинопоиск", "lang": "ru"},
    {"url": "https://www.kinonews.ru/rss.php", "name": "KinoNews", "lang": "ru"},
    {"url": "https://www.filmz.ru/rss/news.xml", "name": "Filmz.ru", "lang": "ru"},
    {"url": "https://www.kino-govno.com/rss", "name": "Кино-Говно", "lang": "ru"},
    
    # Англоязычные (будут переведены)
    {"url": "https://deadline.com/feed/", "name": "Deadline", "lang": "en"},
    {"url": "https://variety.com/feed/", "name": "Variety", "lang": "en"},
    {"url": "https://www.hollywoodreporter.com/feed/", "name": "THR", "lang": "en"},
    {"url": "https://screenrant.com/feed/", "name": "ScreenRant", "lang": "en"},
    {"url": "https://collider.com/feed/", "name": "Collider", "lang": "en"},
    {"url": "https://www.indiewire.com/feed/", "name": "IndieWire", "lang": "en"},
]

# ---- Настройки контента ----
MAX_NEWS_AGE_DAYS = 7          # Удалять новости старше N дней
MAX_NEWS_COUNT = 20            # Максимум новостей на сайте
MAX_AUDIO_DURATION_SEC = 600   # Макс. длина аудио (10 мин)
SUMMARY_MAX_CHARS = 500        # Макс. длина текста для озвучки

# ---- TTS (озвучка) ----
TTS_VOICE = "ru-RU-DmitryNeural"     # Мужской голос
TTS_VOICE_ALT = "ru-RU-SvetlanaNeural"  # Женский голос (альтернативный)
TTS_RATE = "+0%"                      # Скорость речи
TTS_VOLUME = "+0%"                    # Громкость
AUDIO_FORMAT = "mp3"                  # Формат аудио

# ---- Пути ----
DATA_DIR = "data"
AUDIO_DIR = "audio"
NEWS_JSON = "data/news.json"
OUTPUT_HTML = "index.html"
TEMPLATE_HTML = "templates/base.html"

# ---- GitHub Pages ----
SITE_TITLE = "Киновекна 2026"
SITE_DESCRIPTION = "Аудио-новости кино — слушай свежие новости киноиндустрии"
SITE_URL = ""  # Заполнится автоматически при деплое

# ---- Anthropic API (опционально, для переписывания новостей) ----
# Если ключ не задан, используется простая обрезка текста
ANTHROPIC_API_KEY = ""  # Или через переменную окружения ANTHROPIC_API_KEY
