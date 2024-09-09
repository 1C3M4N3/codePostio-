import math

def areaTriangle(base, height):
    calculatedArea = 0.5 * base * height
    return round(calculatedArea, 2)

def areaRectangle(length, width):
    calculatedArea = length * width
    return round(calculatedArea, 2)

def areaCircle(radius):
    calculatedArea = math.pi * radius ** 2
    return round(calculatedArea, 2)

print(areaTriangle(12, 14.4)) #returns 86.4
print(areaRectangle(13.2, 4.5)) #returns 59.4
print(areaCircle(52.1))# returns 8527.57
