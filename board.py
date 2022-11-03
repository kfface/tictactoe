import os

def CheckForWinner(winCond, win, moveCount):
    winCond = list(map(int, str(winCond)))
    winCond = sorted(winCond)
    topRow = [1,2,3]
    midRow = [4,5,6]
    bottomRow = [7,8,9]
    leftCol = [1,4,7]
    midCol = [2,5,8]
    rightCol = [3,6,9]
    diagnal1 = [1,5,9]
    diagnal2 = [3,5,7]
    winCondList = [topRow, midRow, bottomRow, leftCol, midCol, rightCol, diagnal1, diagnal2]
    if winCond is not None:
         result =  all(elem in winCondList for elem in winCond)
    if result:
        print(result)
        win = 1
        return win
    else:
        print("no win")
        


    
def PrintBoard(positions):
    print(positions[1] + "|" + positions[2] + "|" + positions[3])
    print("-----")
    print(positions[4] + "|" + positions[5] + "|" + positions[6])
    print("-----")
    print(positions[7] + "|" + positions[8] + "|" + positions[9])
    print()

def ClearBoard():
    clear = lambda : os.system('tput reset')