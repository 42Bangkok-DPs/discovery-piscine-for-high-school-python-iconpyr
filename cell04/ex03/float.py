#!/usr/bin/env python3
def check_number(number):
    if number.is_integer():
        print ("This number is integer")
    else:
        print ("This number is decimal")

num = (input("Give me number : "))

try:
    number = float(num)
    check_number(number)
except ValueError:
    print("Error")
