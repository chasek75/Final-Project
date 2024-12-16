def createBoard(boardSize):
    board = []
    for row in range(boardSize):
        board.append([])
        for col in range(boardSize):
            board[row].append(0)
    return board

def printBoard(world):
    outputString = "" #empty string
    board = world["board"]
    for row in range(len(board)):
        
        for col in range(len(board)):
            if world["playerloc"]["x"]== col and world["playerloc"]["y"]== row:
                outputString += f"[{"X":2}]"
            elif world["enemy1loc"]["x"]== col and world["enemy1loc"]["y"]== row:
                outputString += f"[{"0 ":2}]"
            elif world["enemy2loc"]["x"]== col and world["enemy2loc"]["y"]== row:
                outputString += f"[{"0 ":2}]"
            elif board[row][col] == 0:
                outputString += f"[{" ":2}]"
        outputString += "\n"
    print(outputString, end="")
    