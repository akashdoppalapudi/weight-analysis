import json
from typing import List
from datetime import date
from Models.weight_record import WeightRecord
from Contracts.json_contract import JSONContract

class JSONService(JSONContract):

    file_path = "data/weight_data.json"

    def readWeightData(self) -> List[WeightRecord]:
        data = []
        with open(self.file_path, 'r') as openfile:
            data = json.load(openfile)
        res = [WeightRecord(date.fromisoformat(wr['date']), float(wr['weight'])) for wr in data]
        return res

    def addWeightData(self, wr: WeightRecord):
        weightData = self.readWeightData()
        weightData.append(wr)
        weightData = sorted(weightData, key=lambda x: x.date)
        exportData = []
        for w in weightData:
            exportData.append({'date': w.date.isoformat(), 'weight': w.weight})
        
        with open(self.file_path, 'w') as outfile:
            json.dump(exportData, outfile, indent=2)
