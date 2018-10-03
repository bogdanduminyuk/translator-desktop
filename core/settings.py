import os


# API settings
application_id = "fadf5485"
application_key = "48fbdacce1908543d0229902ed1917e9"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# parsing settings
urls = {
    "synonym;antonym": "https://od-api.oxforddictionaries.com/api/v1/entries/en/{word_id}/synonyms;antonyms",
    "definitions": "https://od-api.oxforddictionaries.com/api/v1/entries/en/{word_id}",
    "translation": "https://wooordhunt.ru/word/{word_id}"
}

headers = {
    "app_id": "fadf5485",
    "app_key": "48fbdacce1908543d0229902ed1917e9",
    "Accept": "application/json",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
}

one_word_selector = ".t_inline_en"
lexical_categories_selectors = {
    "header":  "h4.pos_item",
    "rows": ["div.tr", "> span"]
}
collocation_selector = ".block.phrases i"

request_timeout = 5
requests_interval = 1

LOG_PATH = "data/log.txt"

values_delimiter = ";"

MAX_CATEGORY_SENSES_COUNT = 20
MAX_ITEMS_COUNT = 7

# USER SETTINGS
MAX_SYNONYMS_DISPLAYED_COUNT = 5
MAX_ANTONYMS_DISPLAYED_COUNT = 5
