import board
class Player():
    def GamePrep (self):
        PlayerName = input("Please enter your name: ")
        PlayersToken = input("Which piece would you like to plays, X or O?")

    def PlayerMove (self, b):
        gettingInput = True
        while gettingInput:
            try:
                selection = int(input("Your turn where would you like to play?: "))
                while selection > 10 or selection < 1 or b.positions[selection] == "X" or b.positions[selection] == "O":
                    selection = int(input("that move is invalid please choose a legal move: "))
                if selection < 10 and selection > 0:
                    gettingInput = False
            except ValueError:
                print("Please select a space on the board 1-9")
            while b.positions[selection] == "X" or  selection > 9 or selection < 0:
                selection = int(input("that move is invalid please choose a legal move: "))
            else:
                b.positions[selection] = "X"
                b.winCondList = [list(map(lambda x: x if x != selection else 'X', i)) for i in b.winCondList]
        return b