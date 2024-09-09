import math

def hypotenuse(num1, num2): 
    return round(math.sqrt(num1 ** 2 + num2 ** 2), 2)


print(hypotenuse(10, 14))