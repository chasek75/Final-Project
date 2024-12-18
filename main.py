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
    global playerloc
    playerloc = {
        "x":0,
        "y":0
    }
    global enemy1loc
    enemy1loc = {
        "x":2,
        "y":0
    }
    global enemy2loc
    enemy2loc = {
        "x":3,
        "y":3
    }
    world["board"] = createBoard(10)
    world["playerloc"] = playerloc
    world["enemy1loc"] = enemy1loc
    world["enemy2loc"] = enemy2loc
    userInput = getUserName()
    world["playerName"] = str(userInput)
    #sets initial score to 0
    scorecount = 0
    hp = health
    #game loop until health runs out
    while hp > 0:
        #Display Board and move user
        if hp > 0:
            printBoard(world)
            userInput = getUserDir()
            if userInput == 'd' and playerloc['x'] < len(world["board"])-1:
                playerloc["x"] += 1
            if userInput == 'a' and playerloc['x'] > 0:
                playerloc["x"] -= 1
            if userInput == 'w' and playerloc['y'] > 0:
                playerloc["y"] -= 1
            if userInput == 's' and playerloc['y'] < len(world["board"])-1:
                playerloc["y"] += 1
        #enemy player tracking function
            enemies()
        #Enemy Player detector + print current health
            if enemy1loc["x"] == playerloc["x"] and enemy1loc["y"] == playerloc["y"]:
                hp -= 1
            if enemy2loc["x"] == playerloc["x"] and enemy2loc["y"] == playerloc["y"]:
                hp -= 1
        #score incresed by 1 per turn
        scorecount += 1
        #convert hp to a string
        hpstring = str(hp)
        #displays hp and player name at the top of the screen while alive
        if hp >= 1:
            print(world["playerName"] + " :HP "+ hpstring +"/3")
        #game over message after health hits 0
        else:
            print("GAME OVER")
            print("Score: " + str(scorecount))
            print("Check the CSV to see score history. Thanks for playing!")
            
            