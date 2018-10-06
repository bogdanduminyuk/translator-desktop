import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER_CFG = os.path.join(BASE_DIR, "user.json")

with open(USER_CFG, "r", encoding="utf-8") as cfg_file:
    user = json.load(cfg_file)


# parsing settings
urls = {
    "synonym;antonym": "https://od-api.oxforddictionaries.com/api/v1/entries/en/{word_id}/synonyms;antonyms",
    "definitions": "https://od-api.oxforddictionaries.com/api/v1/entries/en/{word_id}",
    "translation": "https://wooordhunt.ru/word/{word_id}"
}

headers = {
    "app_id": user["general"]["application_id"],
    "app_key": user["general"]["application_key"],
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

LOG_PATH = "data/log.txt"

# Database settings
db_urls = {
    "count": "http://bogdanduminyuk.pythonanywhere.com/count",
    "get": "http://bogdanduminyuk.pythonanywhere.com/get_word",
    "set": "http://bogdanduminyuk.pythonanywhere.com/set_word",
}
