import math

def hypotenuse(num1, num2): 
    return round(math.sqrt(num1 ** 2 + num2 ** 2), 2)


print(hypotenuse(10, 14))

def main():
    sideOne = float(input("Enter side 1: ").strip())
    sideTwo = float(input("Enter side 2: ").strip())

    calculatedHypotenuse = hypotenuse(sideOne, sideTwo)

    print("The hypotenuse is: ", calculatedHypotenuse)


main()