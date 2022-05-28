from datetime import date

class WeightRecord:
    def __init__(self, date: date, weight: float):
        self.date = date
        self.weight = weight