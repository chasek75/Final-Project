from boardTools import *
from inputProcess import *

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
    world["board"] = createBoard(15)
    world["playerloc"] = playerloc
    world["enemy1loc"] = enemy1loc
    world["playerName"] = getUserName()
    health = 100

    while True:
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
    
        #HP tracking
        maxhp = str(health)
        print("HP remaining:"+ maxhp +"/100")

main()