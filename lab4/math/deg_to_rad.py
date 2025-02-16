from math import radians

degree = None

while degree is None:
    try:
        degree = float(input("Input degree: "))
    except ValueError:
        print("Only numbers allowed! Try again!")

print("Output radian:", round(radians(degree), 6))