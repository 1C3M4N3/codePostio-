import math

def propertyTax(num):
    assessmentVal = num * .6
    finalResult = round(assessmentVal / 100 * .56, 2)
    return finalResult

print(propertyTax(50000))