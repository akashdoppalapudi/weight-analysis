from Models.weight_record import WeightRecord
from Contracts.cli_contract import CLIContract
from datetime import date
from colorama import Fore

class CLI(CLIContract):

    def getInitChoice(self) -> int:
        print(Fore.WHITE + "\n\nSelect an option\n1. Show Analysis\n2. Enter New Record\n3. Exit")
        try:
            res = int(input("Your Choice : "))
        except(Exception):
            raise Exception("Invalid Choice! Only Numericals are allowed.")

        if res<=0 or res>3:
            raise Exception("Invalid Choice! Select from the given options.")

        return res

    def getWeightData(self) -> WeightRecord:
        print(Fore.WHITE + "\n\nNew Weight Record")
        date_str = input("Enter date of record ('yyyy-MM-dd') : ")
        try:
            dt = date.fromisoformat(date_str)
        except(Exception):
            raise Exception("Invalid date format")
        
        try:
            weight = float(input("Enter Weight : "))
        except(Exception):
            raise Exception("Invalid Input")

        return WeightRecord(dt, weight)