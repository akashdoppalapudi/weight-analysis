from abc import ABC, abstractmethod
from Models.weight_record import WeightRecord

class CLIContract(ABC):

    @abstractmethod
    def getInitChoice(self) -> int:
        pass

    @abstractmethod
    def getWeightData(self) -> WeightRecord:
        pass