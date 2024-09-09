
def zipZapZop():
    userInput = int(input("Enter a number: ").strip())

    #create an empty string and concatenate the results
    result = ""
    if userInput % 3 == 0:
        result += "zip"
    if userInput % 5 == 0:
        result += "zap"
    if userInput % 7 == 0:
        result += "zop"

    print(not result and userInput or result) 

zipZapZop()