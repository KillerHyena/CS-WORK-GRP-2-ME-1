#Create a module that contains functions for mathematical operations
import math
def add(a, b):
    """Returns the sum of two numbers"""
    return a + b
def subtract(a, b):
    """Returns the difference of two numbers"""
    return a - b
def multiply(a, b):
    """Returns the product of two numbers"""
    return a * b
def divide(a, b):
    """Returns the division of two numbers"""
    return a / b if b != 0 else "Error! Division by zero is not allowed."
def power(base, exponent):
    """Returns base raised to the power of exponent"""
    return base ** exponent
def factorial(n):
    """Returns factorial of a number"""
    if n < 0:
        return "Factorial not defined for negative numbers."
    return math.factorial(n)
if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("\nMathematical Operations:")
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")
    num = int(input("\nEnter a number to find its factorial: "))
    print(f"Factorial of {num} is {factorial(num)}")
    base = int(input("\nEnter base number: "))
    exponent = int(input("Enter exponent: "))
    print(f"{base} ^ {exponent} = {power(base, exponent)}")