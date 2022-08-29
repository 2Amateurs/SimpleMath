import math


def vector():
    operation = float(input('Press 1 to find components, 2 to find angle and magnitude, 3 for scaling/addition, and 4 for addition with angle and magnitude info.' + '\n'))

    if operation == 1:
        hypotenuse = float(input('Vector magnitude: '))
        angle = float(input('Angle: '))

        i = hypotenuse * math.cos(math.radians(angle))
        j = hypotenuse * math.sin(math.radians(angle))

        print(str(i) + "i")
        print(str(j) + "j")
    elif operation == 2:
        i = float(input('i component: '))
        j = float(input('j component: '))

        hypotenuse = math.sqrt(i**2+j**2)
        if i != 0:
            angle = math.degrees(math.atan(j/i))
            angle = (angle, angle + 180)
        else:
            angle = (90, 270)

        print('magnitude: ' + str(hypotenuse))
        print('angle: ' + str(angle))
    elif operation == 3:
        firstI = float(input('First vector i: '))
        firstJ = float(input('First vector j: '))
        firstScalar = float(input('First scalar: '))
        secondI = float(input('Second vector i: '))
        secondJ = float(input('Second vector j: '))
        secondScalar = float(input('Second scalar: '))
        firstI *= firstScalar
        firstJ *= firstScalar
        secondI *= secondScalar
        secondJ *= secondScalar
        newVectorI = firstI + secondI
        newVectorJ = firstJ + secondJ
        print('i: ' + str(newVectorI))
        print('j: ' + str(newVectorJ))
    else:
        hypotenuse1 = float(input('1st vector magnitude: '))
        angle1 = float(input('1st angle: '))
        i1 = hypotenuse1 * math.cos(math.radians(angle1))
        j1 = hypotenuse1 * math.sin(math.radians(angle1))
        hypotenuse2 = float(input('2nd vector magnitude: '))
        angle2 = float(input('2nd angle: '))
        i2 = hypotenuse2 * math.cos(math.radians(angle2))
        j2 = hypotenuse2 * math.sin(math.radians(angle2))
        newI = i1+i2
        newJ = j1+j2
        print(str(newI)+'i')
        print(str(newJ)+'j')
while True:
    vector()
