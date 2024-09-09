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

def main():
    taffyWeight = float(input("Enter weight of taffy in pounds: "))
    fudgeWeight = float(input("Enter weight of fudge in pounds: "))
    pralineWeight = float(input("Enter weight of praline in pounds: "))

    taffyCost, fudgeCost, pralineCost = costTaffy(taffyWeight), costFudge(fudgeWeight), costPraline(pralineWeight)

    #this number has to be re rounded for whatever reason
    calculatedTotal = round(taffyCost + fudgeCost + pralineCost, 2)

    print("Your total is: ", calculatedTotal)


main()