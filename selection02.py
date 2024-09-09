def canDivideNoRem(dividend, divisor):
    if divisor == 0:
        return False  
    return dividend % divisor == 0

print(canDivideNoRem(44, 4))#returns True
print(canDivideNoRem(20, 3))#returns False