def taxiFare(baseRate, mileRate, totalMiles):
    return round(baseRate + mileRate * totalMiles, 2)

print(taxiFare(3.15, 1.20, 30))