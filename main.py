#main loop where game runs
#sends and revieves variables from the other python files
from boardTools import *
from inputProcess import *
from Enemies import *
import random


global health
#main fuction responsible for moving player and enemies as well as keeping track of score and health
def mainworld():
    #generate world dictionary and inputing board and locational data
    health = 3
    world = {}
    #inputs location values
    global playerloc
    playerloc = {"x":0,"y":0}
    global enemy1loc
    enemy1loc = {"x":2,"y":0}
    global enemy2loc
    enemy2loc = {"x":3,"y":3}
    global freezeloc
    freezeloc = {"x":5,"y":5}
    global shieldloc
    shieldloc = {"x":5,"y":5}
    world["board"] = createBoard(10)
    world["playerloc"] = playerloc
    world["enemy1loc"] = enemy1loc
    world["enemy2loc"] = enemy2loc
    world["freezeloc"] = freezeloc
    world["sheildloc"] = shieldloc
    #get username from user and input into world dictionary
    userInput = getUserName()
    world["playerName"] = str(userInput)
    #sets initial score to 0
    scorecount = 0
    hp = health
    #create power up variables to determine if power up are active and set them to false
    global Freeze
    Freeze = bool
    Freeze = False
    global Sheild
    Sheild = bool
    Sheild = True

    #game loop until health runs out
    while hp > 0:
        #Display Board and move user while health is above 0
        if hp > 0:
            printBoard(world)
            #enemy player tracking function
            enemies()
            #get userinput and adjusts player location
            userInput = getUserDir()
            if userInput == 'd' and playerloc['x'] < len(world["board"])-1:
                playerloc["x"] += 1
            if userInput == 'a' and playerloc['x'] > 0:
                playerloc["x"] -= 1
            if userInput == 'w' and playerloc['y'] > 0:
                playerloc["y"] -= 1
            if userInput == 's' and playerloc['y'] < len(world["board"])-1:
                playerloc["y"] += 1      
        #Enemy Player detector + print current health
        #if shield is on no dmg is taken
            if Sheild == False:
                if enemy1loc["x"] == playerloc["x"] and enemy1loc["y"] == playerloc["y"]:
                    hp -= 1
                if enemy2loc["x"] == playerloc["x"] and enemy2loc["y"] == playerloc["y"]:
                    hp -= 1
        #score incresed by 1 per turn
        scorecount += 1
        #convert hp to a string
        hpstring = str(hp)
        #displays hp in red and player name in default at the top of the screen while alive
        if hp >= 1:
            print(world["playerName"] + " : ",end="")
            print("\033[31m",end="")
            print("HP "+ hpstring +"/3",end="")
            print("\033[0m",end="")
            if Freeze == True:
                print("\033[36m",end="")
                print(" Freeze" + "\033[0m")
                print("\033[0m",end="")
            else:
                print()
        #red game over message and green score display after health hits 0
        else:
            print("\033[31m",end="")
            print("GAME OVER",end="")
            print("\033[0m")
            print("\033[32m",end="")
            print("Score: " + str(scorecount))
            print("\033[0m",end="")
            print("Check the CSV to see score history. Thanks for playing!")

            
            
            