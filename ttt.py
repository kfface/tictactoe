import random


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

def userMove():
    selection = int(input("Your turn where would you like to play?: "))
    while selection > 10 or selection < 0:
        selection = int(input("that move is invalid please choose a legal move: "))
    while positions[selection] == "X" or  selection > 9 or selection < 0:
        selection = int(input("that move is invalid please choose a legal move: "))
    else:
        positions[selection] = "X"
        global winCondList
        winCondList = [list(map(lambda x: x if x != selection else 'X', i)) for i in winCondList]

def checkForWinner():
    for list in winCondList:
        if list[0] == list [1] and list[0] == list[2]:
            if list[0] == "X":
                print("You are the winner!")
                exit()
            elif list[0] == "O":
                print("Get wrecked nerd!")
                exit()


printBoard()
userTurn = True
moveCount = 0


while moveCount < 9:
    if userTurn == True:
        userMove()
        printBoard()
        moveCount += 1
        checkForWinner()
        userTurn = False
        
    else:
        compMove = random.choice(list(positions))
        while positions[compMove] == "O" or positions[compMove] == "X":
            compMove = random.choice(list(positions))
        positions[compMove] = "O"
        winCondList = [list(map(lambda y: y if y != compMove else 'O', i)) for i in winCondList]

        printBoard()
        moveCount += 1
        checkForWinner()
        userTurn = True

