from core.input_data_readers import TxtFileReader
from core.result_data_writers import TxtDataWriter
from core.functions import get_translation, get_word_from_api

input_path = "data/one_line_words.txt"
output_path = "data/output.txt"

if __name__ == "__main__":
    reader = TxtFileReader()
    writer = TxtDataWriter(output_path)
    output = {}

    data = reader.read(input_path)

    print("Read data from file: ", input_path)

    for word in data:
        synonyms, antonyms, definitions = get_word_from_api(word)
        translations = get_translation(word)

        output[word] = {
            "synonyms": synonyms,
            "antonyms": antonyms,
            "definitions": definitions,
            "translations": translations,
        }

        print(word + ".. OK")

    writer.write(output)
    print("OK")
    print("Look for result file: ", output_path)
