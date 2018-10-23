import time

i = 0


def get(word):
    time.sleep(0.2)
    global i
    i += 1

    if i % 2 == 0:
        raise KeyError("Обращение по неверному индексу")
    else:
        return {
            "word": word,
            "syn": word + " synonyms",
            "ant": word + " antonyms",
            "def": word + " definitions",
            "translate": word + " translation"
        }
