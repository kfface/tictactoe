import player
from board import CheckForWinner, PrintBoard, ClearBoard
from computer import ComputerStarterMoves, ComputerMoveWinOrBlock


#make board
positions = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}

#lists for 3 consecutive moves
winCond = []
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
while win == 0:
    if userTurn == True:
        winCondPlayer = player.Player().PlayerMove(positions, winCond)
        PrintBoard(positions)
        print(winCondPlayer)
        moveCount += 1
        winCond = winCondPlayer
        try:
            win = CheckForWinner(win, moveCount, winCond)
        except:
            pass
        userTurn = False
    else:
        noBestMove = True
        if noBestMove == True:
            winCondComp = ComputerStarterMoves(positions)
            noBestMove = False
        else: winCondComp = ComputerMoveWinOrBlock(positions, noBestMove, userTurn, winCond, winCondList)
        print(winCondComp)
        PrintBoard(positions)
        winCond = winCondComp
        try:
            win = CheckForWinner(win, moveCount, winCond)
        except:
            pass
        userTurn = True
        moveCount += 1

