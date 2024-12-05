'''
getUserDir asks the user to enter a direction from
a list of directions. It will continue to ask for directions
so long as the user does not enter a valid direction
Parameters: 
nothing
Returns:
the user inputed direction
'''
def getUserDir():

    validCommands = ['w','a','s','d']
    while True:
        userInput = input("Enter a direction (w,a,s,d): ")
        userInput = userInput.lower().strip()
        if userInput not in validCommands:
            print("Not a valid command")
            continue
        return userInput
'''
getUserName:
asks the user to name their character
Does not allow names larger than 12 characters
Does not allow names smaller than 3 characters
returns that name
Parameters:
nothing
Return:
name user picked

'''
def getUserName():
    while True:
        userInput = input("What's the name of your character?\n:")
        userInput = userInput.upper().strip()
        if len(userInput) > 12:
            print("12 characters or less please")
            continue
        if len(userInput) < 3:
            print("Can't have a name less than three characters")
            continue

        return userInput