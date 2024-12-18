import random
#preforms enemy movement calculations
#imports player and enemy locations from main
#returns new enemy locations based on player location
def enemies():
    #imports needed values from main
    from main import playerloc
    from main import enemy1loc
    from main import enemy2loc
    #enemy 1 will do 1 of 3 options (move in x,y or not at all)
    enemy1xy = random.choice([0, 2])
    #enemy1 moves in x direction towards playerlocation
    if enemy1xy == 0:
                if enemy1loc["x"] > playerloc["x"]:
                    enemy1loc["x"] -= 1
                if enemy1loc["x"] < playerloc["x"]:
                    enemy1loc["x"] += 1
                if enemy1loc["x"] == playerloc["x"] and enemy1loc["y"] < playerloc["y"]:
                    enemy1loc["y"] += 1
                if enemy1loc["x"] == playerloc["x"] and enemy1loc["y"] > playerloc["y"]:
                    enemy1loc["y"] -= 1
    #enemy1 moves in y direction towards playerlocation
    if enemy1xy == 1:
                if enemy1loc["y"] > playerloc["y"]:
                    enemy1loc["y"] -= 1
                if enemy1loc["y"] < playerloc["y"]:
                    enemy1loc["y"] += 1
                if enemy1loc["y"] == playerloc["y"] and enemy1loc["x"] < playerloc["x"]:
                    enemy1loc["x"] += 1
                if enemy1loc["y"] == playerloc["y"] and enemy1loc["x"] > playerloc["x"]:
                    enemy1loc["x"] -= 1
    #enemy1 wont move
    if enemy1xy == 2:
                enemy1loc["x"] += 0
                    
    
    #enemy 2 player tracking
    #enemy2 will do 1 of 3 options (move in x,y or not at all)
    enemy2xy = random.choice([0, 2])
    #enemy2 moves in x direction towards playerlocation
    if enemy2xy == 0:
                if enemy2loc["x"] > playerloc["x"]:
                    enemy2loc["x"] -= 1
                if enemy2loc["x"] < playerloc["x"]:
                    enemy2loc["x"] += 1
                if enemy2loc["x"] == playerloc["x"] and enemy2loc["y"] < playerloc["y"]:
                    enemy2loc["y"] += 1
                if enemy2loc["x"] == playerloc["x"] and enemy2loc["y"] > playerloc["y"]:
                    enemy2loc["y"] -= 1
    #enemy 2 moves in y direction towards playerlocation
    if enemy2xy == 1:
                if enemy2loc["y"] > playerloc["y"]:
                    enemy2loc["y"] -= 1
                if enemy2loc["y"] < playerloc["y"]:
                    enemy2loc["y"] += 1
                if enemy2loc["y"] == playerloc["y"] and enemy2loc["x"] < playerloc["x"]:
                    enemy2loc["x"] += 1
                if enemy2loc["y"] == playerloc["y"] and enemy2loc["x"] > playerloc["x"]:
                    enemy2loc["x"] -= 1
    #enemy2 wont move
    if enemy2xy == 3:
                enemy2loc["x"] += 0