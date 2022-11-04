import os

class Board():
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

    userTurn = True
    moveCount = 0
    thereIsWinner = False
    userTurn = True
    moveCount = 0
    thereIsWinner = False

    def CheckForWinner(self, b):
        for list in b.winCondList:
            if list[0] == list[1] and list[0] == list[2]:
                if list[0] == "X":
                    print("You are the winner!")
                    thereIsWinner = True
                    exit()
                elif list[0] == "O":
                    print("Get wrecked nerd!")
                    thereIsWinner = True
                    exit()
            else:
                if b.moveCount == 9 and thereIsWinner == False:
                    print("It's a draw")
                    exit()
        
    def PrintBoard(self, positions):
        print(positions[1] + "|" + positions[2] + "|" + positions[3])
        print("-----")
        print(positions[4] + "|" + positions[5] + "|" + positions[6])
        print("-----")
        print(positions[7] + "|" + positions[8] + "|" + positions[9])
        print()
        self.moveCount += 1

    def ClearBoard(self):
        clear = lambda : os.system('tput reset')