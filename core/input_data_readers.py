import os

from .abstracts import InputDataReader


class TxtFileReader(InputDataReader):
    def read(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(path)

        with open(path, "r", encoding="utf-8") as file:
            data = file.read().split(",")

            for i in range(len(data)):
                data[i] = data[i].strip()
            return data
