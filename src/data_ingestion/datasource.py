from abc import ABC, abstractmethod

class DataSource(ABC):
    """
    Abstract base class for data sources.
    """
    @abstractmethod
    def read(self):
        pass