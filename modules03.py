#import the random library
import random

#generate a random int set the values to 10 + 1 to not include 10, and 20 - 1 to exclude 20 from the results
number = random.randint(11, 19)

#display the result of the randomly generated number, between 10 and 20 but not including 10 or 20
print("The randomly generated number is:", number)