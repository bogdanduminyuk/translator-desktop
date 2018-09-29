import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup as bs
from . import settings
from .json_answer_parser import *


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


def get_translation(word):
    """
    Realizes parsing WoooordHunt html response depending of input word type.
    Single word or collocation of words.

    :param word: html text of response
    :return: data structure of result
    """
    response_text = request(word, "translation")
    if not response_text:
        return []

    soup = bs(response_text, features="html.parser")
    selector = settings.collocation_selector if is_collocation(word) else settings.one_word_selector
    selection = soup.select(selector)
    result = ""

    for i in selection:
        result = result + i.text + "; "

    # remove last '; ' symbols
    return result[:-2]


def log(word, url, message):
    """
    Writes and log row to a file specified in settings.

    :param word: current word where an error event was happened
    :param url:  current url of request
    :param message: error message
    :return: None
    """
    date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    log_row = "{time}, {word}, {url}, {message}\n".format(time=date_time, word=word, url=url, message=message)
    with open(settings.LOG_PATH, "a", encoding="utf-8") as log_file:
        log_file.write(log_row)


def request(word, key):
    url = settings.urls[key].format(word_id=word)
    response = requests.get(url, headers=settings.headers, timeout=settings.request_timeout)

    if response.ok:
        return response.text
    elif response.status_code == 404:
        log(word, url, "Word cannot be found, status  code: " + str(response.status_code))
    else:
        log(word, url, "Requests error! Status code: " + str(response.status_code))

    return ""


def get_word_from_api(word):
    synonyms, antonyms = "", ""

    if not is_collocation(word):
        response_text = request(word, "synonym;antonym")
        synonyms, antonyms = get_synonyms_antonyms(get_senses_list(response_text))

    response_text = request(word, "definitions")
    definitions = get_definitions(get_senses_list(response_text))

    time.sleep(settings.requests_interval)
    return synonyms, antonyms, definitions


if __name__ == "__main__":
    pass
