import math
import time
import functools


def multiply_list(numbers):
    return functools.reduce(lambda x, y: x * y, numbers)


def casecounter(s):
    up = sum(1 for l in s if l.isupper())
    low = sum(1 for l in s if l.islower())
    return {"Uppercase": up, "Lowercase": low}


def is_palindrome(s):
    return s == s[::-1]


def delsqrt(number, delay):
    time.sleep(delay / 1000)
    return math.sqrt(number)


def all_true(t):
    return all(t)

print(multiply_list([3, 7, 5, 2, 3]))  # Output: 630
print(casecounter("STOP rUnNiNg"))  # Output: {'Uppercase': 7, 'Lowercase': 4}
print(is_palindrome("racecar"))  # Output: True
print(f"Square root of 25100 after 2123 milliseconds is {delsqrt(25100, 2123)}")
print(all_true((True, True, False)))  # Output: False