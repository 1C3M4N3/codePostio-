#import the random library
import random

#initialize and set our first die, each side is theoretically just a number
die1 = random.randint(1, 6)

#do the same for our identical die
die2 = random.randint(1, 6)

#display the random results
print("You rolled two dice:", die1, "and", die2)