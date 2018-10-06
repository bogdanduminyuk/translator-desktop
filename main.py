from core.input_data_readers import TxtFileReader
from core.result_data_writers import DocDataWriter
from core.functions import get_translation, get_word_from_api
from core.db import Database

input_path = "data/input.txt"
output_path = "data/output.docx"

if __name__ == "__main__":
    reader = TxtFileReader()
    writer = DocDataWriter(output_path, {
        "def": True,
        "syn": True,
        "ant": True
    })
    output = {}

    data = reader.read(input_path)

    print("Read data from file: ", input_path)

    for word in data:
        from_db = Database.get(word)

        if from_db:
            output[word] = from_db
        else:
            output[word] = {
                "api": get_word_from_api(word)[0],
                "translation": get_translation(word),
            }

            Database.set(word, output[word]["translation"], output[word]["api"][0])

        print(word + ".. OK")

    writer.write(output)
    print("OK")
    print("Look for result file: ", output_path)
