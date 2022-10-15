import random

#make board
positions = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}

def printBoard():
    print(positions[1] + "|" + positions[2] + "|" + positions[3])
    print("-----")
    print(positions[4] + "|" + positions[5] + "|" + positions[6])
    print("-----")
    print(positions[7] + "|" + positions[8] + "|" + positions[9])
    print()

printBoard()
userTurn = True
moveCount = 0

def userMove():
    selection = int(input("Your turn wher would you like to play?: "))
    positions[selection] = "X"

while moveCount < 9:
    if userTurn == True:
        userMove()
        printBoard()
        moveCount += 1
        userTurn = False
        
    else:
        compMove = random.choice(list(positions))
        while positions[compMove] == "O" or positions[compMove] == "X":
            compMove = random.choice(list(positions))
        positions[compMove] = "O"
        printBoard()
        moveCount += 1
        userTurn = True

