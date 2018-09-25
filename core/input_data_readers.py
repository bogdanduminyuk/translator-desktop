import os

from .abstracts import InputDataReader


class TxtFileReader(InputDataReader):
    def read(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(path)

        with open(path, "r") as file:
            data = file.read().split(",")

            for i in range(len(data)):
                data[i] = data[i].strip()
            return data
