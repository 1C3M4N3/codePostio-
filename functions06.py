import math

def paintJobEstimator(sqrFeet, hourlyCost, gallonPrice):
    paintGallons = (sqrFeet / 110)
    
    laborHours = paintGallons * 8
    
    paintCost = paintGallons * gallonPrice

    laborCost = laborHours * hourlyCost

    totalCost = paintCost + laborCost

    return round(totalCost, 2)
    


print( paintJobEstimator(200, 15, 25) )