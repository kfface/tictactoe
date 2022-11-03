import player
import computer
import random
from board import CheckForWinner, PrintBoard, ClearBoard


#make board
positions = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}

#lists for 3 consecutive moves
winCondPlayer = []
winCondComp = []
topRow = [1,2,3]
midRow = [4,5,6]
bottomRow = [7,8,9]
leftCol = [1,4,7]
midCol = [2,5,8]
rightCol = [3,6,9]
diagnal1 = [1,5,9]
diagnal2 = [3,5,7]
winCondList = [topRow, midRow, bottomRow, leftCol, midCol, rightCol, diagnal1, diagnal2]
win = 0

#start game cycle
player.Player().GamePrep()
PrintBoard(positions)
userTurn = True
moveCount = 0


while moveCount < 10 and win == 0:
    if userTurn == True:
        winCondPlayer = player.Player().PlayerMove(positions, winCondPlayer)
        PrintBoard(positions)
        print(winCondPlayer)
        print(winCondComp)
        moveCount += 1
        win = CheckForWinner(win, winCondPlayer, winCondComp, moveCount)
        userTurn = False
    else:
        noBestMove = True
        computer.Computer().ComputerMoveWinOrBlock(positions, noBestMove, userTurn, winCondComp, winCondList)
        if noBestMove == True:
            winCondComp = computer.Computer().ComputerStarterMoves(positions, winCondComp)
            noBestMove = False
        PrintBoard(positions)
        win = CheckForWinner(win, moveCount, winCondPlayer, winCondComp)
        userTurn = True
        moveCount += 1

