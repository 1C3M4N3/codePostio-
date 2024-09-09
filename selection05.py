import statistics

def middle(*numbers):
    #ha
    numArr = [*numbers]
    return statistics.median(numArr)

print(middle(35, 1, 32))# returns 32
print(middle(14, 9, 45))# returns 14