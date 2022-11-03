import board
import player
import computer
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

#start game cycle
b = board.Board()
p = player.Player()
c = computer.Computer()

b.PrintBoard(positions)

userTurn = True
moveCount = 0


while moveCount < 10:
    if userTurn == True:
        p.PlayerMove(positions, winCondList)
        b.PrintBoard(positions)
        moveCount += 1
        b.CheckForWinner(winCondList, moveCount, thereIsWinner)
        userTurn = False
        
    else:
        noBestMove = True
        c.ComputerMoveWinOrBlock(positions, noBestMove, userTurn, winCondList)
        

        if noBestMove == True:
            c.ComputerStarterMoves(positions, winCondList)
            noBestMove = False
        b.PrintBoard(positions)
        b.CheckForWinner(winCondList, moveCount, thereIsWinner)
        userTurn = True
        moveCount += 1

