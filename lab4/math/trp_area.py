import math

h = float(input("Height: "))
b1 = float(input("Base, first value: "))
b2 = float(input("Base, second value: "))

def trapezoid(height, base1, base2):
    area = ((base1+base2)/2)*height
    return area

print("Expected Output:", trapezoid(h, b1, b2))