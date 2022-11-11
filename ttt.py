import board
import player
import computer
import random




#initialize objects
b = board.Board()
p = player.Player()
c = computer.Computer()

#start game cycle
b.PrintBoard(b.positions)

while b.moveCount < 10:
    if b.userTurn == True:
        b = p.PlayerMove(b)
        b.PrintBoard(b.positions)
        b.userTurn = False
        
    else:
        c.noBestMove = True
        b = c.GetComputersMove(b)
        b.PrintBoard(b.positions)
        b.userTurn = True
    
    b.PrintBoard(b.positions)
    b.UpdateMoveCount()
    b.CheckForWinner()