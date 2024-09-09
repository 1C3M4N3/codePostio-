#import our math library
import math

#get our area of the garden from the users input and strip it then convert it to a float
area = float(input("Please enter the area of the garden: ").strip())

#take the square root of our area and multiply the value by the amount of sides in a square (HINT: that MIGHT be four idk) and store the result
total_fence = math.sqrt(area) * 4

#display the result to the user
print( "You will need", total_fence, "meters of fence" )
