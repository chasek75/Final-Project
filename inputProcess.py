
def getUserDir():

    validCommands = ['w','a','s','d']
    while True:
        userInput = input("Enter a direction (w,a,s,d): ")
        userInput = userInput.lower().strip()
        if userInput not in validCommands:
            print("Not a valid command")
            continue
        return userInput

def getUserName():
    while True:
        userInput = input("What's the name of your character?\n:")
        userInput = userInput.upper().strip()
        if len(userInput) > 12:
            print("12 characters or less please")
            continue
        if len(userInput) < 3:
            print("More than 3 characters please")
            continue

        return userInput