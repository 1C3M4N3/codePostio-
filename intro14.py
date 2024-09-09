# Retrieve inputs

# Retrieve the amount due
amountDue = int(input("Enter the amount due in pennies: ").strip())

# Retrieve the amount received from the customer
amountReceived = int(input("Enter the amount received from the customer in pennies: ").strip())

# Define the values of the coins in pennies
nQuarter = 25  # quarter
nDime = 10     # dime
nNickel = 5    # nickel

# Calculate total change to return
calculatedChange = amountReceived - amountDue  

# Calculate the number of dollars to return
dollarAmount = calculatedChange // 100  # There are 100 pennies in a dollar
remainingChange = calculatedChange % 100  # Remaining change after dollars

# Calculate the number of quarters to return
quarterAmount = remainingChange // nQuarter  # Number of quarters
remainingChange = remainingChange % nQuarter  # Remaining change after quarters

# Calculate the number of dimes to return
dimeAmount = remainingChange // nDime  # Number of dimes
remainingChange = remainingChange % nDime  # Remaining change after dimes

# Calculate the number of nickels to return
nickelAmount = remainingChange // nNickel  # Number of nickels
pennyAmount = remainingChange % nNickel  # Remaining change after nickels (will be the number of pennies)

# Print the results
print("Give the following change to the customer:")
print(dollarAmount, "dollars,", quarterAmount, "quarters,", dimeAmount, "dimes,", nickelAmount, "nickels and", pennyAmount, "pennies")