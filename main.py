from boardTools import *
from inputProcess import *
from Enemies import *
import random

def main():
    world = {}
    playerloc = {
        "x":0,
        "y":0
    }
    enemy1loc = {
        "x":5,
        "y":0
    }
    enemy2loc = {
        "x":10,
        "y":10
    }
    world["board"] = createBoard(15)
    world["playerloc"] = playerloc
    world["enemy1loc"] = enemy1loc
    world["enemy2loc"] = enemy2loc
    world["playerName"] = getUserName()
    health = 100
    

    while health > 0:
        #Display Board and move user
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
        #enemy 1 ai
        enemy1xy = random.choice([0, 1])
        if enemy1xy == 0:
            if enemy1loc["x"] > playerloc["x"]:
                enemy1loc["x"] -= 1
            if enemy1loc["x"] < playerloc["x"]:
                enemy1loc["x"] += 1
        if enemy1xy == 1:
            if enemy1loc["y"] > playerloc["y"]:
                enemy1loc["y"] -= 1
            if enemy1loc["y"] < playerloc["y"]:
                enemy1loc["y"] += 1
        #enemy 2 ai
        enemy2xy = random.choice([0, 1])
        if enemy2xy == 0:
            if enemy2loc["x"] > playerloc["x"]:
                enemy2loc["x"] -= 1
            if enemy2loc["x"] < playerloc["x"]:
                enemy2loc["x"] += 1
        if enemy2xy == 1:
            if enemy2loc["y"] > playerloc["y"]:
                enemy2loc["y"] -= 1
            if enemy2loc["y"] < playerloc["y"]:
                enemy2loc["y"] += 1

        #Enemy collision detector + print current health
        if enemy1loc["x"] == playerloc["x"] and enemy1loc["y"] == playerloc["y"]:
            health -= 10
        if enemy2loc["x"] == playerloc["x"] and enemy2loc["y"] == playerloc["y"]:
            health -= 10
        maxhp = str(health)
        if health > 0:
            print(world["playerName"] + ":HP "+ maxhp +"/100")
        else:
            print("GAME OVER")


main()