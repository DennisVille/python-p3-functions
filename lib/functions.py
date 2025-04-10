#!/usr/bin/env python3

def greet_programmer():
    print('Hello, programmer!')

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    sum = num1 + num2
    return sum

def halve(number):
    if not isinstance(number, (int, float)):
    #if type(number) != int or type(number) != float:
        return None
    return number / 2


