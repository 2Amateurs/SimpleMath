import math

def solve():
    a = float(input('a value: '))
    b = float(input('b value: '))
    c = float(input('c value: '))
    sqrt = b**2-4*a*c
    if sqrt < 0:
        print("(" + str(-b) + " + sqrt(" +  str(math.sqrt(-sqrt)) + ")i" + ")/" + str(2*a) + ", " + "(" + str(-b) + " - sqrt(" +  str(math.sqrt(-sqrt)) + ")i" + ")/" + str(2*a))
    else:
        print(str((-b+math.sqrt(sqrt))/(2*a)) + ", " + str((-b-math.sqrt(sqrt))/(2*a)))

while True:
    solve()
