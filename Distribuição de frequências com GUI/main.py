from control.data import info
from interface.main_menu import mainScreen
from interface.results_screen import results

while True:
    freqDistribution = info()

    mainMenu = mainScreen()
    mainMenu.startInterface()

    freqDistribution.setClass(mainMenu.classInput)
    freqDistribution.setNums(mainMenu.numInput)

    result = results()
    result.recieveClasses(freqDistribution.classes())
    result.recieveFrequencies(freqDistribution.frequency())
    result.recieveRelativeFreqs(freqDistribution.relativeFreq())
    result.recieveCumulativeFreqs(freqDistribution.cumulativeFreq())
    result.startInterface()

# Classes exercício: 7
# Números exercício: 50 40 41 17 11 7 22 44 28 21 19 23 37 51 54 42 86 41 78 56 72 56 17 7 69 30 80 56 29 33 46 31 39 20 18 29 34 59 73 77 36 39 30 62 54 67 39 31 53 44