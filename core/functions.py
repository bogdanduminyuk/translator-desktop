from datetime import datetime

from . import settings
from bs4 import BeautifulSoup as bs


def is_collocation(char_sequence):
    """
    Check if the char sequence is collocation.
    :param char_sequence: sequence of characters
    :return: True if char_sequence is collocation else False
    """
    min_length, space, max_space_count = 2, " ", 1

    if len(char_sequence) < min_length or char_sequence.count(space) != max_space_count:
        return False

    lexemes = char_sequence.split(space)

    for lexeme in lexemes:
        if not lexeme.isalpha():
            return False

    return True


def get_translation(text, collocation):
    """
    Realizes parsing WoooordHunt html response depending of input word type.
    Single word or collocation of words.

    :param text: html text of response
    :param collocation: bool parameter indicated if the searched word is collocation or not
    :return: data structure of result
    """
    # TODO: improve it to parse both single word and its collocations
    selector = settings.collocation_selector if collocation else settings.one_word_selector
    soup = bs(text, features="html.parser")
    selection = soup.select(selector)
    result = ""

    for i in selection:
        result = result + i.text + "; "

    # remove last '; ' symbols
    return result[:-2]


def log(word, url, message):
    date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    log_row = "{time}, {word}, {url}, {message}\n".format(time=date_time, word=word, url=url, message=message)
    with open(settings.LOG_PATH, "a", encoding="utf-8") as log_file:
        log_file.write(log_row)


if __name__ == "__main__":
    pass
