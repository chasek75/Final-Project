#this file creates the game board list and prints the game board with player and enemy locations

#inputs board size from main
#creates empty game board list
def createBoard(boardSize):
    board = []
    for row in range(boardSize):
        board.append([])
        for col in range(boardSize):
            board[row].append(0)
    return board


#inputs are player and enemy locations
#output prints the game board with player and enemies in thier correct locations
def printBoard(world):
    outputString = "" 
    board = world["board"]
    for row in range(len(board)):
        for col in range(len(board)):
            #Detects if the player is on the same tile as an enemy
            #will change the output string to show both the player and the enemy
            if world["playerloc"]["x"]== col and world["playerloc"]["y"]== row:
                    if world["enemy1loc"]["x"] == world["playerloc"]["x"] and world["enemy1loc"]["y"] == world["playerloc"]["y"]:
                        outputString += f"[{"X0":2}]"
                    elif world["enemy2loc"]["x"] == world["playerloc"]["x"] and world["enemy2loc"]["y"] == world["playerloc"]["y"]:
                        outputString += f"[{"X0":2}]"
                    elif world["enemy3loc"]["x"] == world["playerloc"]["x"] and world["enemy3loc"]["y"] == world["playerloc"]["y"]:
                         outputString += f"[{"X0":2}]"
                    elif world["enemy1loc"]["x"] != world["playerloc"]["x"] or world["enemy1loc"]["y"] != world["playerloc"]["y"]:
                        outputString += f"[{"X ":2}]"
            #Shows Sheild powerup location
            elif world["sheildloc"]["x"] == col and world["sheildloc"]["y"] == row:
                 outputString += f"[{"S ":2}]"
            #Shows freeze powerup location
            elif world["freezeloc"]["x"] == col and world["freezeloc"]["y"] == row:
                 outputString += f"[{"F ":2}]"
            #detects if multiple enemies are on the same tile
            #will change the output string to show both enemies
            elif world["enemy1loc"]["x"] == col and world["enemy1loc"]["y"] == row:
                    if world["enemy1loc"]["x"] == world["enemy2loc"]["x"] and world["enemy1loc"]["y"] == world["enemy2loc"]["y"]:
                        outputString += f"[{"00":2}]"
                    if world["enemy1loc"]["x"] == world["enemy3loc"]["x"] and world["enemy1loc"]["y"] == world["enemy3loc"]["y"]:
                        outputString += f"[{"00":2}]"    
                    else:
                        outputString += f"[{"0 ":2}]"
            elif world["enemy2loc"]["x"]== col and world["enemy2loc"]["y"] == row:
                    if world["enemy1loc"]["x"] == world["enemy2loc"]["x"] and world["enemy1loc"]["y"] == world["enemy2loc"]["y"]:
                        outputString += f"[{"00":2}]"
                    if world["enemy2loc"]["x"] == world["enemy3loc"]["x"] and world["enemy2loc"]["y"] == world["enemy3loc"]["y"]:
                        outputString += f"[{"00":2}]"
                    else:
                        outputString += f"[{"0 ":2}]"
            elif world["enemy3loc"]["x"] == col and world["enemy3loc"]["y"] == row:
                    if world["enemy3loc"]["x"] == world["enemy1loc"]["x"] and world["enemy3loc"]["y"] == world["enemy1loc"]["y"]:
                        outputString += f"[{"00":2}]"
                    if world["enemy3loc"]["x"] == world["enemy2loc"]["x"] and world["enemy3loc"]["y"] == world["enemy2loc"]["y"]:
                        outputString += f"[{"00":2}]"
                    else:
                        outputString += f"[{"0 ":2}]"
            elif board[row][col] == 0:
                outputString += f"[{" ":2}]"
        outputString += "\n"
    print(outputString, end="")
    