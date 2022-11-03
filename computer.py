import random
import board

class Computer():
    #picks a 'random' move when no block or win move is available
    #the middle space has the highest weight followed by the four corners
    def StarterMoves (self, b):
        priorityMoveAvailable = False
        priorityMoves = [5,1,3,7,9]
        for value in priorityMoves:
            if b.positions[value] != "X" and b.positions[value] != "O":
                compMove = value
                b.positions[compMove] = "O"
                priorityMoveAvailable = True
                break
        if priorityMoveAvailable == False:
            compMove = random.choice(list(b.positions))
            while b.positions[compMove] == "O" or b.positions[compMove] == "X":
                compMove = random.choice(list(b.positions))
                b.positions[compMove] = "O"
        
        b.winCondList = [list(map(lambda y: y if y != compMove else 'O', i)) for i in b.winCondList]
        return b.winCondList

    def GetComputersMove(self, b):
        
        noBestMove = True
        self.MoveWinOrBlock(noBestMove, b)

        if noBestMove == True:
            self.StarterMoves(b)
            noBestMove = False

    def MoveWinOrBlock(self, noBestMove, b):
        for list in b.winCondList:
            xCounter = 0
            oCounter = 0
            for value in list:
                if value == "O":
                    oCounter += 1
                if oCounter == 2:
                    for index, item in enumerate(list):
                        if list[index] != "O" and list[index] != "X":
                            compMove = list[index]
                            b.positions[list[index]] = "O"
                            noBestMove = False
                            break
        for list in b.winCondList:
            xCounter = 0
            oCounter = 0
            for value in list:
                if value == "X":
                    xCounter += 1
                if xCounter == 2:
                    for index, item in enumerate(list):
                        if list[index] != "O" and list[index] != "X":
                            compMove = list[index]
                            b.positions[list[index]] = "O"
                            noBestMove = False
                            break
        if noBestMove == False:
            for i in b.winCondList:
                for v in list:
                    if v == compMove:
                        i[list.index(v)] = 'O'

            #b.winCondList = [list(map(lambda y: y if y != int(compMove) else 'O', i)) for i in b.winCondList]
        return b.winCondList
       