from .abstracts import ResultDataWriter


class TxtDataWriter(ResultDataWriter):
    def __init__(self, path):
        self.path = path

    def write(self, data):
        with open(self.path, "w", encoding="utf-8") as file:
            for key, value in data.items():
                file.write(key + ": " + str(value) + "\n")
