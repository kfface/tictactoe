import board
import random
class Computer():
    #picks a 'random' move when no block or win move is available
    #the middle space has the highest weight followed by the four corners
    def ComputerStarterMoves (self, positions, winCondComp):
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
        winCondComp.append(compMove)
        return winCondComp
        
    def ComputerMoveWinOrBlock (self, positions, noBestMove, userTurn, winCondComp, winCondList):
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
        if noBestMove == False:
            winCondComp.append(compMove)
            return winCondComp
       