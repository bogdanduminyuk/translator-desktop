import abc


class InputDataReader(metaclass=abc.ABC):
    """ Interface for analyzing of input data. """
    @abc.abstractmethod
    def read(self, data):
        """
        :return: internal python structure (list, dict, set, etc.) of input data.
        """


class ResultDataWriter(metaclass=abc.ABC):
    """ Interface for writing data to something. """
    @abc.abstractmethod
    def write(self, data):
        """
        :return: True if data was writen else False
        """


class DataSaver(metaclass=abc.ABC):
    """ Interface for saving data to something like cache, database, etc. """
    @abc.abstractmethod
    def save(self, data):
        """
        The method realizes the process of saving data.
        :param data: data to save
        :return: True if success else False
        """

    @abc.abstractmethod
    def get(self, keyword):
        """
        It uses go get data from cache, db, etc (if exists).
        :param keyword: key to find in storage
        :return: value for keyword if the keyword exists in storage else False
        """
