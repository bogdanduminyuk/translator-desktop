import time
import requests
from bs4 import BeautifulSoup as bs
from core import settings
from core.input_data_readers import OneLineReader
from core.result_data_writers import TxtDataWriter

input_path = "data/one_line_words.txt"
output_path = "data/output.txt"

reader = OneLineReader()
writer = TxtDataWriter(output_path)
data = reader.read(input_path)
url = settings.urls["translation"]
output = {}

print("Read data from file: ", input_path)

for word in data:
    response = requests.get(url.format(word_id=word), headers=settings.headers, timeout=settings.request_timeout)

    if response.ok:
        soup = bs(response.text, features="html.parser")
        selection = soup.select(settings.selector)

        if selection:
            selection = selection[0].text

        print("'{}': '{}'".format(word, selection))
        output[word] = selection
        time.sleep(0.33)
    else:
        raise ConnectionError(response)

writer.write(output)
print("OK")
print("Look for result file: ", output_path)
