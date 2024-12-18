from boardTools import *
from inputProcess import *
from Enemies import *
import random


def mainworld():
    #generate world dictionary and input starting positions
    world = {}
    global playerloc
    playerloc = {
        "x":0,
        "y":0
    }
    global enemy1loc
    enemy1loc = {
        "x":5,
        "y":0
    }
    global enemy2loc
    enemy2loc = {
        "x":10,
        "y":10
    }
    world["board"] = createBoard(15)
    world["playerloc"] = playerloc
    world["enemy1loc"] = enemy1loc
    world["enemy2loc"] = enemy2loc
    world["playerName"] = "Chase"
    health = 3
    
    #game loop until health runs out
    while health >= 0:
        #Display Board and move user
        if health >= 0:
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
            #enemy 1 player tracking
            enemies()
            #Enemy Player detector + print current health
            if enemy1loc["x"] == playerloc["x"] and enemy1loc["y"] == playerloc["y"]:
                health -= 1
            if enemy2loc["x"] == playerloc["x"] and enemy2loc["y"] == playerloc["y"]:
                health -= 1
            print(health)
        if health <= 0:
            health -= 1
            print("game over")

            
mainworld()