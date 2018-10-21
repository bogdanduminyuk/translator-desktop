import time


def get(word):
    time.sleep(0.2)
    return {
        "word": word,
        "syn": word + " synonyms",
        "ant": word + " antonyms",
        "def": word + " definitions",
        "translate": word + " translation"
    }
