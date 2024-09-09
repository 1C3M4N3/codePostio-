#prices per pound
taffyPrice = 5.99
fudgePrice = 9.99
pralinePrice = 8.99


def costTaffy(flPounds):
    return round(taffyPrice * flPounds, 2)

def costFudge(flPounds):
    return round(fudgePrice * flPounds, 2)


def costPraline(flPounds):
    return round(pralinePrice * flPounds, 2)


print(costTaffy(5.5)) #returns 32.95
print(costFudge(8)) #returns 79.92
print(costPraline(2.3))# returns 20.68