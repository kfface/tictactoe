from functools import partial
import os
import tkinter as tk
from tkinter.constants import DISABLED, NORMAL

class Board():

    buttons = [None] * 10

    def clicked(buttons, buttonNumber):
        #TODO: Implement 
        print(buttonNumber)
        buttons[buttonNumber]['state'] = DISABLED
        buttons[buttonNumber]['text'] = 'X'

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
    
    window = tk.Tk()
    window.title("Tic Tac Toe")
    window.resizable(width=False, height=False)
    
    for i in range(3):
        for j in range(3):
            frame = tk.Frame(
                master=window,
                width=20,
                height=10,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j, padx=5, pady=5)
            buttonNumber = ((3*i) + (j+1))
            button = tk.Button(master=frame, background="grey", text="-", command=partial(clicked, buttons, buttonNumber))
            button.pack(padx=5, pady=5)
            buttons[buttonNumber] = button

    window.mainloop()

    

    def PrintBoard(self):
        #clear the terminal before printing out the board state
        os.system('cls' if os.name == 'nt' else 'clear')

        print(self.positions[1] + "|" + self.positions[2] + "|" + self.positions[3])
        print("-----")
        print(self.positions[4] + "|" + self.positions[5] + "|" + self.positions[6])
        print("-----")
        print(self.positions[7] + "|" + self.positions[8] + "|" + self.positions[9])
        print()