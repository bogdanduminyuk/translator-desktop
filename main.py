from core.input_data_readers import OneLineReader

reader = OneLineReader()
data = reader.read("data/one_line_words.txt")
print(data)

