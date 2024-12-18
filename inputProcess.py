
# gets user input and returns it to mainworld function
def getUserDir():

    validCommands = ['w','a','s','d']
    while True:
        userInput = input("Enter a direction (w,a,s,d): ")
        userInput = userInput.lower().strip()
        #user input validation ensures user can only enter movement commands
        if userInput not in validCommands:
            print("Not a valid command")
            continue
        return userInput
# gets username as input and returns it to mainworld function
def getUserName():
    while True:
        userInput = input("What's the name of your character?\n:")
        userInput = userInput.upper().strip()
        #user input validation ensures length of username is 3-12 characters
        if len(userInput) > 12:
            print("12 characters or less please")
            continue
        if len(userInput) < 3:
            print("More than 3 characters please")
            continue

        return userInput