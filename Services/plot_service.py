from Models.weight_record import WeightRecord
from Contracts.plot_contract import PlotContract
import matplotlib.pyplot as plt
from typing import List

class PlotService(PlotContract):
    def plotWeightData(self, weightData: List[WeightRecord]):
        dates = []
        weights = []

        for wr in weightData:
            dates.append(wr.date)
            weights.append(wr.weight)
        
        plt.figure(figsize=(15, 15))
        plt.plot(dates, weights)
        plt.xlabel("Date")
        plt.ylabel("Weight")
        plt.title("Weight Analysis")
        plt.show()