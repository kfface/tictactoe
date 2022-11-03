import os
class Board():
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
        
    def PrintBoard(self):
        #clear the terminal before printing out the board state
        os.system('cls' if os.name == 'nt' else 'clear')

        print(self.positions[1] + "|" + self.positions[2] + "|" + self.positions[3])
        print("-----")
        print(self.positions[4] + "|" + self.positions[5] + "|" + self.positions[6])
        print("-----")
        print(self.positions[7] + "|" + self.positions[8] + "|" + self.positions[9])
        print()

    def ClearBoard(self):
        clear = lambda : os.system('tput reset')
    
    