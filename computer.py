import random
class Computer():
    #picks a 'random' move when no block or win move is available
    #the middle space has the highest weight followed by the four corners
    def StarterMoves (self, positions, winCondList):
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
        return winCondList

    def GetComputersMove(self, positions, winCondList):
        
        noBestMove = True
        self.MoveWinOrBlock(positions, noBestMove, winCondList)

        if noBestMove == True:
            self.StarterMoves(positions, winCondList)
            noBestMove = False

    def MoveWinOrBlock (self, positions, noBestMove, winCondList):
        for list in winCondList:
            xCounter = 0
            oCounter = 0
            for value in list:
                if value == "O":
                    oCounter += 1
                if oCounter == 2:
                    for index, item in enumerate(list):
                        if list[index] != "O" and list[index] != "X":
                            compMove = list[index]
                            positions[list[index]] = "O"
                            noBestMove = False
        for list in winCondList:
            xCounter = 0
            oCounter = 0
            for value in list:
                if value == "X":
                    xCounter += 1
                if xCounter == 2:
                    for index, item in enumerate(list):
                        if list[index] != "O" and list[index] != "X":
                            compMove = list[index]
                            positions[list[index]] = "O"
                            noBestMove = False
        if noBestMove == False:
            winCondList = [list(map(lambda y: y if y != compMove else 'O', i)) for i in winCondList]
        return winCondList
       