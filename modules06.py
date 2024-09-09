#import our math lib
import math

#init our area variable, then prompt the user for the area of a pizza then convert it to a float, then strip it
diameter = float(input("Enter the diameter of the pizza: ").strip())

#calculate the radius from the diameter
radius = diameter / 2

#calculate our area by multiplying math.pi with the area and multiplying that by 2 (pi * area ^ 2)
area = (math. pi * (radius ** 2))

#display the results to the user
print("The area of the pizza is:", area)