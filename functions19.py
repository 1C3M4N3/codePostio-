#print the banner
print("Welcome to the CSU Taco Shop!")

#predifine the prices before tax
beefTaco = 2.90
shrimpTaco = 3.00
fishTaco = 3.25
chickenTaco = 2.75
lentilTaco = 2.50

#store tuples with the menu items in an array
menu = [
    ("Barbeque beef taco", beefTaco),
    ("Shrimp and grits taco", shrimpTaco),
    ("Cajun fish taco", fishTaco),
    ("Chicken guacamole taco", chickenTaco),
    ("Caramelized onion lentil taco", lentilTaco)
]

#create our function to loop through our menu items and display them in the proper format
def drawMenu():
    print("Menu:")
    for item, price in menu:
        print(f"{item:<30} ${price:.2f}")

def beef_taco(itemQuant): #i hate
  #multiply item quant by unit price
  return itemQuant * beefTaco

def shrimp_taco(itemQuant): #snake case
  #multiply item quant by unit price
  return itemQuant * shrimpTaco

def fish_taco(itemQuant): #so
  #multiply item quant by unit price
  return itemQuant * fishTaco

def chicken_taco(itemQuant): #much
  #multiply item quant by unit price
  return itemQuant * chickenTaco

def lentil_taco(itemQuant): #bleh
  #multiply item quant by unit price
  return itemQuant * lentilTaco

#draw our final order
def drawFinalOrder(orderArr):
    print("Your order is:")
    for quant, item in orderArr:
        print(quant, item)

def main():
    drawMenu()

    beefTacoQaunt = int(input("How many barbeque beef tacos would you like? ").strip())
    shrimpTacoQuant = int(input("How many shrimp and grits tacos would you like? ").strip())
    fishTacoQuant = int(input("How many cajun fish tacos would you like? ").strip())
    chickenTacoQuant = int(input("How many chicken guacamole tacos would you like? ").strip())
    lentilTacoQuant = int(input("How many caramelized onion lentil tacos would you like? ").strip())

    calcBefore = round(beefTaco * beefTacoQaunt + shrimpTaco * shrimpTacoQuant + fishTaco * fishTacoQuant + chickenTaco * chickenTacoQuant + lentilTaco * lentilTacoQuant, 2)
    calcAfter = round(calcBefore * 1.08, 2)

    #store the order into an array of tuples
    storedOrder = [    
        (beefTacoQaunt, "Barbeque beef taco"),
        (shrimpTacoQuant, "Shrimp and grits taco"),
        (fishTacoQuant, "Cajun fish taco"),
        (chickenTacoQuant, "Chicken guacamole taco"),
        (lentilTacoQuant, "Caramelized onion lentil taco")
    ]

    drawFinalOrder(storedOrder)
    print("Your total before tax is ", f"${calcBefore:.2f}")
    print("Your total after tax is ", f"${calcAfter:.2f}")





# Write a main() function that gets user input, utilizes all of the above working 
# helper functions, and calculates total price before and after tax.
main()