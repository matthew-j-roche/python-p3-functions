#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    pass

def greet(name):
    print(f"Hello, {name}!")
    pass

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    pass

def add(num1, num2):
    return num1 + num2
    pass

def halve(number):
    return number / 2
    pass

def my_function(param):
    print("Running my_function")
    return param + 1

my_function_return_value = my_function(1)

print(my_function_return_value)