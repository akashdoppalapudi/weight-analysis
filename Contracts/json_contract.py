from abc import ABC, abstractmethod
from typing import List
from Models.weight_record import WeightRecord

class JSONContract(ABC):

    @abstractmethod
    def readWeightData(self) -> List[WeightRecord]:
        pass

    @abstractmethod
    def addWeightData(self, wr: WeightRecord):
        pass