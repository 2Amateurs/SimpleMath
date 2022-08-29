import math

triangle = []

degree = ""

def addValue():
    currentDegree = 0
    while currentDegree < degree+1:
        value = []
        value.append(1)
        if currentDegree > 0:
            i = 0
            while i < (currentDegree-1):
                value.append(triangle[currentDegree-1][i]+triangle[currentDegree-1][i+1])
                i+=1
            value.append(1)
        triangle.append(value)
        currentDegree += 1

def findChars(lineNum):
    chars = len(triangle[lineNum]) + 1
    for item in triangle[lineNum]:
        chars += len(str(item))
    return chars
        
def printTriangle(lineNum):
    if lineNum == 0:
        print()
    offset = math.floor((findChars(len(triangle)-1)-findChars(lineNum))/2)
    print("/")
    printValue = ""
    for whiteSpaces in range(offset):
        printValue += " "
    for item in triangle[lineNum]:
        printValue += (" " + str(item))
    print(printValue)
    print("/")
    if lineNum < len(triangle)-1:
        printTriangle(lineNum + 1)
    else:
        print()
        
while True:    
    triangle = []  
    degree = int(input("Please input to what degree you would like to display" + "\n"))
    addValue()
    printTriangle(0)

