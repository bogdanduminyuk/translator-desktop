import os

from .abstracts import InputDataReader


class TxtFileReader(InputDataReader):
    def read(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(path)

        with open(path, "r", encoding="utf-8") as file:
            return PlainTextReader().read(file.read())


class PlainTextReader(InputDataReader):
    def read(self, plain_text):
        data_list = plain_text.split(",")

        for i in range(len(data_list)):
            data_list[i] = data_list[i].strip()

        return data_list
