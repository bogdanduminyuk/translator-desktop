import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup as bs
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
    result = {
        "simple": "",
        "collocations": [],
        "lexicalCategories": []
    }

    for i in soup.select(settings.one_word_selector):
        result["simple"] += i.text + "; "

    # remove last '; ' symbols
    result["simple"] = result["simple"][:-2]

    headers = soup.select(settings.lexical_categories_selectors["header"])
    rows = soup.select(settings.lexical_categories_selectors["rows"][0])

    for header, row in zip(headers, rows):
        translations = row.select(settings.lexical_categories_selectors["rows"][1])
        result["lexicalCategories"].append({
            "lexicalCategory": header.text[:-2],
            "translations": [translation.text for translation in translations]
        })

    result["collocations"] = [collocation.text for collocation in soup.select(settings.collocation_selector)]
    return result


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
    """
    Makes a request to url from settings.url by given key.

    :param word: word to get
    :param key: key of settings.url dict
    :return: response.text if success else empty string
    """
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
    """
    Realizes requests for Oxford API to get synonyms, antonyms and definitions.

    :param word: word to get
    :return: result dictionary with grouping by lexical entries
    """
    response_text = request(word, "definitions")
    definitions_dict = get_definitions(get_senses_list(response_text))

    if not is_collocation(word):
        response_text = request(word, "synonym;antonym")
        syn_ant = get_synonyms_antonyms(get_senses_list(response_text))

        # sync definitions and synonyms|antonyms lexical categories
        for def_result in definitions_dict:
            for syn_ant_result in syn_ant:
                for def_lexical_entry in def_result["lexicalEntries"]:
                    for syn_ant_lexical_entry in syn_ant_result["lexicalEntries"]:
                        if def_lexical_entry["lexicalCategory"] == syn_ant_lexical_entry["lexicalCategory"]:
                            def_lexical_entry.update(syn_ant_lexical_entry)

    time.sleep(settings.requests_interval)
    return definitions_dict


if __name__ == "__main__":
    pass
