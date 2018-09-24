import os

from .abstracts import InputDataReader


class OneLineReader(InputDataReader):
    def read(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(path)

        with open(path, "r") as file:
            data = file.read()
            return data.split(',')
