import math

def findXY():
    print('ax + by = c' + '\n' + 'dx + ey = f')
    a = float(input('a coefficient: '))
    b = float(input('b coefficient: '))
    c = float(input('c: '))
    d = float(input('f coefficient: '))
    e = float(input('e coefficient: '))
    f = float(input('f: '))
    x = (c*e-b*f)/(a*e-b*d)
    y = (a*f-c*d)/(a*e-b*d)
    print('x: ' + str(x))
    print('y: ' + str(y))

while True:
    findXY()
