import time


def get(word):
    time.sleep(1)
    return {
        "word": word,
        "syn": word + " synonyms",
        "ant": word + " antonyms",
        "def": word + " definitions",
    }
