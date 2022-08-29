import math

def removeSpaces(string):
    string = string.replace(" ", "")
    return string

point1 = input("Enter a point value in the form (a, b)" + "\n")

point1 = removeSpaces(point1)

i = 1
x1 = ""

while not point1[i] == ",":
    x1 += point1[i]
    i += 1

