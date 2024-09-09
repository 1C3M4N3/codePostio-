def speeding(driverSpeed, speedLimit):
    if driverSpeed <= speedLimit:
        return "No speed violation"
    
    overViolation = driverSpeed - speedLimit

    calculatedTicket = 50 + overViolation * 4

    if overViolation >= 25:
        calculatedTicket += 300

    if driverSpeed >= 90:
        calculatedTicket += 150

    return calculatedTicket

print(speeding(75, 60))# returns 110
print(speeding(90, 75))# returns 260
print(speeding(50, 25))# returns 450
print(speeding(35, 40))# returns 'No speed violation'