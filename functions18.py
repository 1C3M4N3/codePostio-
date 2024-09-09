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

def main():
    triangleBase = float(input("Enter the base of the triangle: ").strip())
    triangleHeight = float(input("Enter the height of the triangle: ").strip())
    
    rectangleLen = float(input("Enter the length of the rectangle: ").strip())
    rectangleWidth = float(input("Enter the width of the rectangle: ").strip())

    circleRadius = float(input("Enter the radius of the circle: ").strip())

    calcTriangle, calcRectangle, calcCircle = areaTriangle(triangleBase, triangleHeight), areaRectangle(rectangleLen, rectangleWidth), areaCircle(circleRadius)

    calcTotal = round(calcTriangle + calcRectangle + calcCircle, 2)

    print("Total area is: ", calcTotal)


main()