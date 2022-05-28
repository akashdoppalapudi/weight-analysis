from abc import ABC, abstractmethod
from typing import List
from Models.weight_record import WeightRecord

class PlotContract(ABC):

    @abstractmethod
    def plotWeightData(self, weightData: List[WeightRecord]):
        pass