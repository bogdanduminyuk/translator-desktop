import time
import requests
from core import settings
from core.input_data_readers import TxtFileReader
from core.result_data_writers import TxtDataWriter
from core.functions import is_collocation, get_translation


input_path = "data/one_line_words.txt"
output_path = "data/output.txt"

if __name__ == "__main__":
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
