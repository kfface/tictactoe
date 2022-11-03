class Player():
    def GamePrep(self):
        PlayerName = input("Please enter your name: ")
        PlayersToken = input("Which piece would you like to plays, X or O?")

    def GetPlayersMove(self, positions, winCondList):

        userInput = input("Your turn where would you like to play?: ")

        if(self.IsInvalidUserInput(userInput, positions)):
            self.GetPlayersMove(positions, winCondList)
        
        #map user selected position
        positions[int(userInput)] = "X"
        
        winCondList = [list(map(lambda x: x if x != int(userInput) else 'X', i)) for i in winCondList]

        #TODO: why was this originally returning winCondList?

    def IsInvalidUserInput(self, userInput, positions):
        try:
            selection = int(userInput)
            if selection > 9 or selection < 1 or positions[selection] == "X" or positions[selection] == "O":
                print("That move is invalid please choose a legal move.")
                return True
           
        except ValueError:
                print("Please select a space on the board 1-9")
                return True

        return False
