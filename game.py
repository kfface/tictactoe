class Game:
    moveCount = 0
    isPlayersTurn = True

    def TurnCompleted(self):
        self.moveCount += 1
        self.isPlayersTurn = True if self.isPlayersTurn == False else False

    def CheckForWinner(self, winCondList):
        for list in winCondList:
            if list[0] == list[1] and list[0] == list[2]:
                if list[0] == "X":
                    print("You are the winner!")
                    exit()
                elif list[0] == "O":
                    print("Get wrecked nerd!")
                    exit()
            else:
                if self.moveCount == 9:
                    print("It's a draw")
                    exit()