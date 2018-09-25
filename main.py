import time
import requests
from bs4 import BeautifulSoup as bs
from core import settings
from core.input_data_readers import TxtFileReader
from core.result_data_writers import TxtDataWriter


def is_collocation(char_sequence):
    collocation = True if word.find(" ") >= 0 else False
    if len(char_sequence):  # TODO: improve it
        pass

    return collocation


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


if __name__ == "__main__":
    input_path = "data/one_line_words.txt"
    output_path = "data/output.txt"

    reader = TxtFileReader()
    writer = TxtDataWriter(output_path)
    output = {}

    data = reader.read(input_path)
    url = settings.urls["translation"]

    print("Read data from file: ", input_path)

    for word in data:
        response = requests.get(url.format(word_id=word), headers=settings.headers, timeout=settings.request_timeout)

        if response.ok:
            translation = get_translation(response.text, is_collocation(word))

            print("'{}': '{}'".format(word, translation))
            output[word] = translation
            time.sleep(0.33)
        else:
            raise ConnectionError(response)

    writer.write(output)
    print("OK")
    print("Look for result file: ", output_path)
