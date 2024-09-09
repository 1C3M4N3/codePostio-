import math

def divWithRem(x, y):
    dividedNums, remainderOf = math.floor(x / y), x % y
    return dividedNums, remainderOf

print(divWithRem(9, 5))