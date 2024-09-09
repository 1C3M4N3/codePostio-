#100, 50, 150 input values
#Class A seats cost $75, Class B seats cost $65, and Class C seats cost $50
def eventSeatSales(seatsA, seatsB, seatsC):
    classA, classB, classC = 75, 65, 50
    classASales = seatsA * classA
    classBSales = seatsB * classB
    classCSales = seatsC * classC
    
    totalIncome = classASales + classBSales + classCSales

    return totalIncome

print(eventSeatSales(100, 50, 150))