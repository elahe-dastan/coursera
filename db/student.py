from abc import ABC, abstractmethod


class StudentTable(ABC):
    @abstractmethod
    def read_table(self):
        pass

    @abstractmethod
    def read_row(self, id):
        pass

    @abstractmethod
    def add_row(self, student):
        pass

    @abstractmethod
    def delete_row(self, id):
        pass

