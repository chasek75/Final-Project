#file gets user inputs, validates them, and returns them to mainworld function

#function gets and verifies directional inputs from user and returns them to main
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
#Function gets and verfifies username and returns it to mainworld function
def getUserName():
    while True:
        userInput = input("Please enter a username(between 3 and 12 characters)\n:")
        userInput = userInput.upper().strip()
        #user input validation ensures length of username is 3-12 characters
        if len(userInput) > 12:
            print("12 characters or less please")
            continue
        if len(userInput) < 3:
            print("More than 3 characters please")
            continue

        return userInput