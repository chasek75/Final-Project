import random
def enemies():
    from main import playerloc
    from main import enemy1loc
    from main import enemy2loc
    enemy1xy = random.choice([0, 2])
    if enemy1xy == 0:
                if enemy1loc["x"] > playerloc["x"]:
                    enemy1loc["x"] -= 1
                if enemy1loc["x"] < playerloc["x"]:
                    enemy1loc["x"] += 1
                if enemy1loc["x"] == playerloc["x"] and enemy1loc["y"] < playerloc["y"]:
                    enemy1loc["y"] += 1
                if enemy1loc["x"] == playerloc["x"] and enemy1loc["y"] > playerloc["y"]:
                    enemy1loc["y"] -= 1
    if enemy1xy == 1:
                if enemy1loc["y"] > playerloc["y"]:
                    enemy1loc["y"] -= 1
                if enemy1loc["y"] < playerloc["y"]:
                    enemy1loc["y"] += 1
                if enemy1loc["y"] == playerloc["y"] and enemy1loc["x"] < playerloc["x"]:
                    enemy1loc["x"] += 1
                if enemy1loc["y"] == playerloc["y"] and enemy1loc["x"] > playerloc["x"]:
                    enemy1loc["x"] -= 1
    if enemy1xy == 2:
                enemy1loc["x"] += 0
                    
            #enemy 2 player tracking
    enemy2xy = random.choice([0, 2])
    if enemy2xy == 0:
                if enemy2loc["x"] > playerloc["x"]:
                    enemy2loc["x"] -= 1
                if enemy2loc["x"] < playerloc["x"]:
                    enemy2loc["x"] += 1
                if enemy2loc["x"] == playerloc["x"] and enemy2loc["y"] < playerloc["y"]:
                    enemy2loc["y"] += 1
                if enemy2loc["x"] == playerloc["x"] and enemy2loc["y"] > playerloc["y"]:
                    enemy2loc["y"] -= 1
    if enemy2xy == 1:
                if enemy2loc["y"] > playerloc["y"]:
                    enemy2loc["y"] -= 1
                if enemy2loc["y"] < playerloc["y"]:
                    enemy2loc["y"] += 1
                if enemy2loc["y"] == playerloc["y"] and enemy2loc["x"] < playerloc["x"]:
                    enemy2loc["x"] += 1
                if enemy2loc["y"] == playerloc["y"] and enemy2loc["x"] > playerloc["x"]:
                    enemy2loc["x"] -= 1
    if enemy2xy == 3:
                enemy2loc["x"] += 0