def taxiFare(baseRate, mileRate, totalMiles):
    return round(baseRate + mileRate * totalMiles, 2)

def main():
    baseRate = float(input("Enter base rate: ").strip())
    mileRate = float(input("Enter cost per mile: ").strip())
    totalMiles = float(input("Enter number of miles traveled: ").strip())

    calculatedFare = taxiFare(baseRate, mileRate, totalMiles)

    print("Your fare is: ", calculatedFare)


main()