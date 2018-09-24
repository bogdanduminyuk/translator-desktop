from .abstracts import DataSaver


class EmptyDataSaver(DataSaver):
    def save(self, data):
        return True

    def get(self, keyword):
        return False
