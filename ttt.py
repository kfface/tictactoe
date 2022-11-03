import board
import player
import computer
import game

#initialize game components
b = board.Board()
p = player.Player()
c = computer.Computer()
g = game.Game()

#start game cycle
b.PrintBoard()

#loop until there is a winner or a draw
#this will always before or at 9 turns
while g.moveCount < 10:
    if g.isPlayersTurn == True:
        p.GetPlayersMove(b)
        
    else:
        c.GetComputersMove(b)
        
    b.PrintBoard()
    g.CheckForWinner(b.winCondList)
    g.TurnCompleted()
