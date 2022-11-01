import random

thereIsWinner = False
#make board
positions = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}

#lists for 3 consecutive moves
topRow = [1,2,3]
midRow = [4,5,6]
bottomRow = [7,8,9]
leftCol = [1,4,7]
midCol = [2,5,8]
rightCol = [3,6,9]
diagnal1 = [1,5,9]
diagnal2 = [3,5,7]
winCondList = [topRow, midRow, bottomRow, leftCol, midCol, rightCol, diagnal1, diagnal2]
def printBoard():
    print(positions[1] + "|" + positions[2] + "|" + positions[3])
    print("-----")
    print(positions[4] + "|" + positions[5] + "|" + positions[6])
    print("-----")
    print(positions[7] + "|" + positions[8] + "|" + positions[9])
    print()

def getUserMove():
    gettingInput = True
    while gettingInput:
        try:
            selection = int(input("Your turn where would you like to play?: "))
            while selection > 10 or selection < 1 or positions[selection] == "X" or positions[selection] == "O":
                selection = int(input("that move is invalid please choose a legal move: "))
            if selection < 10 and selection > 0:
                gettingInput = False
        except ValueError:
            print("Please select a space on the board 1-9")
    while positions[selection] == "X" or  selection > 9 or selection < 0:
        selection = int(input("that move is invalid please choose a legal move: "))
    else:
        positions[selection] = "X"
        global winCondList
        winCondList = [list(map(lambda x: x if x != selection else 'X', i)) for i in winCondList]

def checkForWinner():
    global winCondList
    global moveCount
    global thereIsWinner
    for list in winCondList:
        if list[0] == list[1] and list[0] == list[2]:
            if list[0] == "X":
                print("You are the winner!")
                thereIsWinner = True
                exit()
            elif list[0] == "O":
                print("Get wrecked nerd!")
                thereIsWinner = True
                exit()
        else:
            if moveCount == 9 and thereIsWinner == False:
                print("It's a draw")
                exit()

def computerStarterMoves ():
    global winCondList
    priorityMoveAvailable = False
    priorityMoves = [5,1,3,7,9]
    for value in priorityMoves:
        if positions[value] != "X" and positions[value] != "O":
            compMove = value
            positions[compMove] = "O"
            priorityMoveAvailable = True
            break
    if priorityMoveAvailable == False:
        compMove = random.choice(list(positions))
        while positions[compMove] == "O" or positions[compMove] == "X":
            compMove = random.choice(list(positions))
            positions[compMove] = "O"
    winCondList = [list(map(lambda y: y if y != compMove else 'O', i)) for i in winCondList]

def computerMoveWinOrBlock ():
    global noBestMove
    global userTurn
    global winCondList
    global compMove
    for list in winCondList:
        xCounter = 0
        oCounter = 0
        if userTurn == True:
            break
        for value in list:
            if value == "O":
                oCounter += 1
            if oCounter == 2:
                for index, item in enumerate(list):
                    if list[index] != "O" and list[index] != "X":
                        compMove = list[index]
                        positions[list[index]] = "O"
                        noBestMove = False
                        userTurn = True
    for list in winCondList:
        xCounter = 0
        oCounter = 0
        if userTurn == True:
            break    
        for value in list:
            if value == "X":
                xCounter += 1
            if xCounter == 2:
                for index, item in enumerate(list):
                    if list[index] != "O" and list[index] != "X":
                        compMove = list[index]
                        positions[list[index]] = "O"
                        noBestMove = False
                        userTurn = True
    
printBoard()
userTurn = True
moveCount = 0


while moveCount < 10:
    if userTurn == True:
        getUserMove()
        printBoard()
        moveCount += 1
        checkForWinner()
        userTurn = False
        
    else:
        noBestMove = True
        computerMoveWinOrBlock()
        if noBestMove == False:
            winCondList = [list(map(lambda y: y if y != compMove else 'O', i)) for i in winCondList]

        if noBestMove == True:
            computerStarterMoves()
            noBestMove = False
        printBoard()
        checkForWinner()
        userTurn = True
        moveCount += 1

