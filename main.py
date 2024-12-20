#main loop where game runs
#sends and revieves variables from the other python files
from boardTools import *
from inputProcess import *
from Enemies import *
import random
import csv
global health

#main fuction responsible for moving player and enemies as well as keeping track of score,health,and powerups
def mainworld():
    #set intitial HP and create world dictionary
    health = 3
    world = {}
    #makes location data global for use in other python files
    global playerloc
    global enemy1loc
    global enemy2loc
    global enemy3loc
    global freezeloc
    global shieldloc
    #reads CSV file and seperates lines
    file = open("CSV.csv","r")
    fileContents = file.read()
    fileLines = fileContents.split("\n")
    fileLines.pop(0)
    #chooses random line to use for starting locations
    gamelistvariable = random.randint(0,4)
    gamedata = fileLines[gamelistvariable].split(",")
    #uses location data picked from CSV for staring positions
    playerloc = {"x":int(gamedata[0]),"y":int(gamedata[1])}
    enemy1loc = {"x":int(gamedata[3]),"y":int(gamedata[4])}
    enemy2loc = {"x":int(gamedata[5]),"y":int(gamedata[6])}
    enemy3loc = {"x":int(gamedata[7]),"y":int(gamedata[8])}
    freezeloc = {"x":int(gamedata[9]),"y":int(gamedata[10])}
    shieldloc = {"x":int(gamedata[11]),"y":int(gamedata[12])}
    #inputs starting data into world dictionary
    world["playerloc"] = playerloc
    world["enemy1loc"] = enemy1loc
    world["enemy2loc"] = enemy2loc
    world["enemy3loc"] = enemy3loc
    world["freezeloc"] = freezeloc
    world["sheildloc"] = shieldloc
    #get username from user and input into world dictionary
    userInput = getUserName()
    world["playerName"] = str(userInput)
    boardsize = getdifficulty()
    world["board"] = createBoard(boardsize)
    #sets initial score to 0
    scorecount = 0
    hp = health
    #create power up variables and set them to 0
    global Freeze
    Freeze = 0
    global Shield
    Shield = 0
    #game loop until health runs out
    while hp > 0:
        #Display Board and move user while health is above 0
        if hp > 0:
            printBoard(world)
            #enemy player tracking unless freeze is on
            if Freeze == 0:
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
        #checks if player is on sheild power up
        # gives player sheild and removes powerup from board   
        if playerloc["x"] == shieldloc["x"] and playerloc["y"] == shieldloc["y"]:
            Shield = 11
            shieldloc["x"] = 20
            shieldloc["y"] = 20
        #checks if player is on freeze power up
        # gives player freeze and removes powerup from board 
        if playerloc["x"] == freezeloc["x"] and playerloc["y"] == freezeloc["y"]:
            Freeze = 11
            freezeloc["x"] = 20
            freezeloc["y"] = 20

        #if shield is on no dmg is taken
        if Shield == 0:
            if enemy1loc["x"] == playerloc["x"] and enemy1loc["y"] == playerloc["y"]:
                    hp -= 1
            if enemy2loc["x"] == playerloc["x"] and enemy2loc["y"] == playerloc["y"]:
                    hp -= 1
            if enemy3loc["x"] == playerloc["x"] and enemy3loc["y"] == playerloc["y"]:
                    hp -= 1
        #score incresed by 1 per turn
        scorecount += 1
        #removes powerup charges each turn
        if Shield > 0:
             Shield -= 1
        if Freeze > 0:
             Freeze -= 1
        #convert hp to a string
        hpstring = str(hp)
        #displays hp in red and player name in default at the top of the screen while alive
        if hp >= 1:
            printBoard(world)
            print(world["playerName"] + " : ",end="")
            print("\033[31m",end="")
            print("HP "+ hpstring +"/3",end="")
            print("\033[0m",end="")
            if Shield > 0:
                print("\033[36m",end="")
                print(" Shield " + str(Shield) + " turns left" + "\033[0m")
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

            
            
            