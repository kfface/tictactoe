import os
class Board():
    def CheckForWinner(self, winCondList, moveCount, thereIsWinner):
        for list in winCondList:
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
                if moveCount == 9 and thereIsWinner == False:
                    print("It's a draw")
                    exit()
        return winCondList
        
    def PrintBoard(self, positions):
        print(positions[1] + "|" + positions[2] + "|" + positions[3])
        print("-----")
        print(positions[4] + "|" + positions[5] + "|" + positions[6])
        print("-----")
        print(positions[7] + "|" + positions[8] + "|" + positions[9])
        print()

    def ClearBoard(self):
        clear = lambda : os.system('tput reset')