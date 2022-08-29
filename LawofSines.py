import math

while True:
    side1 = float(input("Side 1:" + "\n"))
    angle1 = float(input("Enter the angle opposite of that side:" + "\n"))


    side2 = input("Side 2 (leave blank if unknown):" + "\n")
    angle2 = input("Enter the known angle (leave blank if unknown)" + "\n")

    operation = 1

    if angle2 == "":
        operation = 2
        side2 = float(side2)
    else:
        angle2 = float(angle2)

    if operation == 1:
        value = (side1 * math.sin(math.radians(angle2)))/math.sin(math.radians(angle1))
        print(value)
    else:
        value = math.degrees(math.asin((side2 * math.sin(math.radians(angle1)))/side1))
        print(str(value) + "\n" + str(180-value))
        



