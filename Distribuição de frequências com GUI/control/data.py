import math

class info:
    def __init__(self):
        self.numbers = []

    def setClass(self, x): # Sets the class
        self.Class = x

    def getClass(self):
        return self.Class

    def setNums(self, nums): # The input will already be an array because of the GUI "main_menu.py"
        self.numbers = nums

    def amplitude(self):
        self.numbers.sort()
        amplitude = self.numbers[-1] - self.numbers[0]
        return amplitude

    def width(self):
        width = self.amplitude() / self.getClass()
        return math.ceil(width)

    def classes(self): # Returns a 2D array with all the numbers from setNums divided in each class.
        self.numbers.sort() 

        startingWidth = self.width() # class / amplitude = width
        width = (startingWidth + self.numbers[0]) - 1
        oldWidth = 0

        arrayClasses = []
        while (width < self.numbers[-1]):

            if(len(arrayClasses) > 0): # Code starts here after having run the frist time; without this, it wouldn't run a final time to get the right result.
                if (oldWidth == 0):
                    oldWidth = width
                else:
                    oldWidth += startingWidth
                width += startingWidth

            Class = []
            for x in range(len(self.numbers)):
                if(self.numbers[x] <= width and self.numbers[x] > oldWidth): # Vai cair aqui se o número estiver no intervalo do K/L=h
                    Class.append(self.numbers[x])
            arrayClasses.append(Class)

        return arrayClasses

    def frequency(self):
        classes = self.classes() # Let's say there's 7 classes, so it'll set here a 2D array with 7 elements.
        total = 0
        freq = []
        for x in range(len(classes)): # Will loop 7 times, because of the len of the 2D array from above.
            freq.append(len(classes[x])) # Then, everytime, it'll grab the len of each sub-array from the 2D array set above.
            total += len(classes[x])
        freq.append(total)
        return freq

    def relativeFreq(self):
        freq = self.frequency()
        relative = []
        for x in range(len(freq)):
            relative.append(freq[x]/freq[-1])
        return relative

    def cumulativeFreq(self):
        freq = self.frequency()
        cumulative = 0
        for x in range(len(freq)):
            cumulative += freq[x]
            freq[x] = cumulative
        return freq 