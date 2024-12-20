import random
#preforms enemy movement calculations
#imports player and enemy locations from main
#returns new enemy locations based on player location
def enemies():
    #imports needed values from main
    from main import playerloc
    from main import enemy1loc
    from main import enemy2loc
    from main import enemy3loc
    from main import Freeze

    #enemy 1 will move in x or y direction unless freeze is active
    enemy1xy = random.randint(0, 2)
    if Freeze == True:
        enemy1xy = 2
    #enemy1 moves in x direction towards playerlocation
    if enemy1xy == 0 :
                if enemy1loc["x"] > playerloc["x"]:
                    enemy1loc["x"] -= 1
                if enemy1loc["x"] < playerloc["x"]:
                    enemy1loc["x"] += 1
                if enemy1loc["x"] == playerloc["x"] and enemy1loc["y"] < playerloc["y"]:
                    enemy1loc["y"] += 1
                if enemy1loc["x"] == playerloc["x"] and enemy1loc["y"] > playerloc["y"]:
                    enemy1loc["y"] -= 1
    #enemy1 moves in y direction towards playerlocation
    if enemy1xy == 1 :
                if enemy1loc["y"] > playerloc["y"]:
                    enemy1loc["y"] -= 1
                if enemy1loc["y"] < playerloc["y"]:
                    enemy1loc["y"] += 1
                if enemy1loc["y"] == playerloc["y"] and enemy1loc["x"] < playerloc["x"]:
                    enemy1loc["x"] += 1
                if enemy1loc["y"] == playerloc["y"] and enemy1loc["x"] > playerloc["x"]:
                    enemy1loc["x"] -= 1
    #enemy1 wont move
    if enemy1xy == 2 :
                enemy1loc["x"] += 0
                    
    
    #enemy 2 player tracking
    #enemy2 will move in either x or y direction unless freeze is active
    enemy2xy = random.randint(0, 2)
    if Freeze == True:
          enemy2xy = 2
    #enemy2 moves in x direction towards playerlocation
    if enemy2xy == 0 :
                if enemy2loc["x"] > playerloc["x"]:
                    enemy2loc["x"] -= 2
                if enemy2loc["x"] < playerloc["x"]:
                    enemy2loc["x"] += 2
                if enemy2loc["x"] == playerloc["x"] and enemy2loc["y"] < playerloc["y"]:
                    enemy2loc["y"] += 2
                if enemy2loc["x"] == playerloc["x"] and enemy2loc["y"] > playerloc["y"]:
                    enemy2loc["y"] -= 2
    #enemy 2 moves in y direction towards playerlocation
    if enemy2xy == 1 :
                if enemy2loc["y"] > playerloc["y"]:
                    enemy2loc["y"] -= 2
                if enemy2loc["y"] < playerloc["y"]:
                    enemy2loc["y"] += 2
                if enemy2loc["y"] == playerloc["y"] and enemy2loc["x"] < playerloc["x"]:
                    enemy2loc["x"] += 2
                if enemy2loc["y"] == playerloc["y"] and enemy2loc["x"] > playerloc["x"]:
                    enemy2loc["x"] -= 2
    #enemy2 wont move
    if enemy2xy == 2 :
                enemy2loc["x"] += 0

    #enemy 3 player tracking
    enemy3xy = random.randint(0, 2)
    if Freeze == True:
          enemy3xy = 2
    #enemy2 moves in x direction towards playerlocation
    if enemy3xy == 0 :
                if enemy3loc["x"] > playerloc["x"]:
                    enemy3loc["x"] -= 1
                if enemy3loc["x"] < playerloc["x"]:
                    enemy3loc["x"] += 1
                if enemy3loc["x"] == playerloc["x"] and enemy3loc["y"] < playerloc["y"]:
                    enemy3loc["y"] += 1
                if enemy3loc["x"] == playerloc["x"] and enemy3loc["y"] > playerloc["y"]:
                    enemy3loc["y"] -= 1
    #enemy 2 moves in y direction towards playerlocation
    if enemy2xy == 1 :
                if enemy3loc["y"] > playerloc["y"]:
                    enemy3loc["y"] -= 1
                if enemy3loc["y"] < playerloc["y"]:
                    enemy3loc["y"] += 1
                if enemy3loc["y"] == playerloc["y"] and enemy3loc["x"] < playerloc["x"]:
                    enemy3loc["x"] += 1
                if enemy3loc["y"] == playerloc["y"] and enemy3loc["x"] > playerloc["x"]:
                    enemy3loc["x"] -= 1
    #enemy2 wont move
    if enemy3xy == 2 :
                enemy3loc["x"] += 0