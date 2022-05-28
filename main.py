from Models.weight_record import WeightRecord
from Services.json_service import JSONService
from Services.plot_service import PlotService
from CLI.CLI import CLI
from colorama import Fore
import colorama

colorama.init()
jsonService = JSONService()
cli = CLI()
plotService = PlotService()

while(True):
    try:
        initChoice = cli.getInitChoice()
        if initChoice == 1:
            weightData = jsonService.readWeightData()
            plotService.plotWeightData(weightData)
        elif initChoice == 2:
            newWR = cli.getWeightData()
            jsonService.addWeightData(newWR)
            print(Fore.GREEN + "\nNew Record Added Successfully!!")
        else:
            break
    except Exception as ex:
        print(Fore.RED + "\n",ex)
