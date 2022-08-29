import math

data = []

class listValue:
    def __init__(self, value, occurences):
        self.value = value
        self.occurences = occurences

def even(value):
    if math.floor(value/2) == value/2:
        return True
    return False

def getList():
    data.clear()
    print("Enter values.  When you're done, press '/' .")
    value = None
    while not (value == '/'):
        value = (input("Enter list value: "))
        if not (value == '/'):
            data.append(float(value))
    if len(data) == 0:
        print("Please provide at least 1 value.")
        getList()

def mean(printValue, data):
    summation = 0
    for number in data:
        summation += number
    meanValue = summation/len(data)
    if printValue:
        print(str(meanValue))
    return meanValue
    

def median(printValue, data):
    data.sort()
    if even(len(data)):
        medianValue = (data[int(len(data)/2)-1] + data[int(len(data)/2)])/2
    else:
        medianValue = data[int(math.floor(len(data)/2))]
    if printValue:
        print(str(medianValue))
    return medianValue

def timesListed(num, array):
    counter = 0
    for number in array:
        if number == num:
            counter += 1
    return counter

def mode(printValue, data):
    bestValue = listValue(0, 0)
    bestValues = []
    summation = 0 
    for number in data:
        times = timesListed(number, data)
        if times > bestValue.occurences:
            bestValues.clear()
            bestValue = listValue(number, times)
            bestValues.append(bestValue)
        elif times == bestValue.occurences:
            bestValues.append(listValue(number, times))
    for item in bestValues:
        summation += item.value
    modeValue = summation/len(bestValues)
    if printValue:
        print(str(modeValue))
    return modeValue

def standardDeviation(printValue, data):
    dataMean = mean(False, data)
    squaredDeviations = []
    for number in data:
        squaredDeviations.append((number-dataMean)**2)
    squaredMean = mean(False, squaredDeviations)
    deviationValue = math.sqrt(squaredMean)
    if printValue:
        print(str(deviationValue))
    return deviationValue
     
def getOperation():
    operation = int(input("Press 1 for mean, 2 for median, 3 for mode, 4 for standard deviation, and 5 to quit and create a new list." + '\n' ))
    if operation == 1:
        mean(True, data)
        getOperation()
    elif operation == 2:
        median(True, data)
        getOperation()
    elif operation == 3:
        mode(True, data)
        getOperation()
    elif operation == 4:
        standardDeviation(True, data)
        getOperation()
    elif operation == 5:
        return
    else:
        print("Please provide a proper input.")
        getOperation()

while True:
    getList()
    data.sort()
    print(data)
    getOperation()

