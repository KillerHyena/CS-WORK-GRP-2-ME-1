# Write a Python program to calculate the area of a circle given the radius
import math
def area(n):
    area = math.pi * (n * n)
    return area
def main():
    radius = float(input("Enter the radius of the circle : "))
    print(f"The area of the circle with radius {radius} is : {area(radius)} sq.units")
main()