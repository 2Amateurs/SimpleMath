import math

while True:
    function = input("Please input the integral function in the form ax^b + C." + "\n")

    a = "0"
    b = "0"
    c = "0"

    i = 0

    def removeSpaces():
        global function
        function = function.replace(" ", "")

    removeSpaces()
    while not function[i] == "x":
        a += function[i]
        i += 1
    i += 2
    while not function[i] == "+":
        b += function[i]
        i += 1
    i += 1
    while i < len(function):
        c += function[i]
        i += 1
    a = float(a)
    b = float(b)
    c = float(c)

    def f(x):
        return a*(x**b)+c

    def area(left, right):
        return f(right)-f(left)

    left = float(input("Enter the left bound" + "\n"))
    right = float(input("Enter the right bound" + "\n"))

    print(area(left, right))
