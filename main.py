# imports
import tkinter as tk
from tkinter import *

roundplay = 0

array = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

tiktaktoe = Tk()

tiktaktoe.geometry("300x300")
tiktaktoe.title("TikTakToe")

tiktaktoe.rowconfigure([0, 1, 2], minsize=90, weight=1)
tiktaktoe.columnconfigure([0, 1, 2], minsize=90, weight=1)

#fill the hole field in winner color
def redwin():
    for row in range(3):
        for column in range(3):
            name = tk.Button(master=tiktaktoe, text="O", font=('times', 35, 'bold'), foreground="red")
            name.grid(row=row, column=column, sticky="nsew")

def bluewin():
    for row in range(3):
        for column in range(3):
            name = tk.Button(master=tiktaktoe, text="X", font=('times', 35, 'bold'), foreground="Blue")
            name.grid(row=row, column=column, sticky="nsew")


#define reset button
def reset(window):
    global array
    global roundplay
    roundplay = 0
    array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for row in range(3):
        for column in range(3):
            name = tk.Button(master=tiktaktoe, text="", command=lambda a=row, b=column: player(a, b),font=('times', 35, 'bold'))
            name.grid(row=row, column=column, sticky="nsew")
            window.destroy()

#extra window to desplay winner
def winner_red():
    win =tk.Toplevel()
    canvas = tk.Label(win, text="Rot gewinnt", font=('times', 35, 'bold'), background="Black", foreground="Red")
    canvas.grid(row=0, column=0)
    resetbutton = tk.Button(win, text="Play again?", command=lambda: reset(win), font=('times', 12, 'bold'))
    resetbutton.grid(row=1, column=0)
    redwin()

def winner_blue():
    win2 =tk.Toplevel()
    canvas = tk.Label(win2, text="Blau gewinnt",font=('times', 35, 'bold'), background="Black", foreground="Blue")
    canvas.grid(row=0, column=0)
    resetbutton = tk.Button(win2, text="Play again?", command=lambda: reset(win2), font=('times', 12, 'bold'))
    resetbutton.grid(row=1, column=0)
    bluewin()

def tie():
    tie =tk.Toplevel()
    canvas = tk.Label(tie, text="Unentschieden", font=('times', 35, 'bold'), background="Black", foreground="White")
    canvas.grid(row=0, column=0)
    resetbutton = tk.Button(tie, text="Play again?", command=lambda: reset(tie), font=('times', 12, 'bold'))
    resetbutton.grid(row=1, column=0)


#putting the right symbol on the button
def player(row, column):
    global roundplay
    global array
    if roundplay == 8:
        tie()
    if roundplay % 2 == 0:
        name = tk.Button(master=tiktaktoe, text="X", font=('times', 35, 'bold'), foreground="blue")
        name.grid(row=row, column=column, sticky="nsew")
        roundplay = roundplay + 1
        array[row][column] = "X"
        checkforwin(name)
    else:
        name = tk.Button(master=tiktaktoe, text="O", font=('times', 35, 'bold'), foreground="red")
        name.grid(row=row, column=column, sticky="nsew")
        roundplay = roundplay + 1
        array[row][column] = "O"
        checkforwin(name)

#defining button for playfield
for row in range(3):
    for column in range(3):
        name = tk.Button(master=tiktaktoe, text="", command=lambda a=row, b=column: player(a, b), font=('times', 35, 'bold'))
        name.grid(row=str(row), column=str(column), sticky="nsew")


#checking for winner
def checkforwin(name):
    for row in range(3):
        #test for winner horizontal
        if array[row][0] == array[row][1] and array[row][1] == array[row][2] and array[row][0] == "X":
            print("Blau gewinnt")
            winner_blue()
            break
        elif array[row][0] == array[row][1] and array[row][1] == array[row][2] and array[row][0] == "O":
            print("Rot gewinnt")
            winner_red()
            break
            #test for winner vertical
        elif array[0][row] == array[1][row] and array[1][row] == array[2][row] and array[0][row] == "X":
            print("Blau gewinnt")
            winner_blue()
            break
        elif array[0][row] == array[1][row] and array[1][row] == array[2][row] and array[0][row] == "O":
            print("Rot gewinnt")
            winner_red()
            break
        #test for winner diagonal1
        elif array[0][0] == array[1][1] and array[1][1] == array[2][2] and array[1][1] == "X":
            print("Blau gewinnt")
            winner_blue()
            break
        elif array[0][0] == array[1][1] and array[1][1] == array[2][2] and array[1][1] == "O":
            print("Rot gewinnt")
            winner_red()
            break
        #test for winner diagonal2
        elif array[0][2] == array[1][1] and array[1][1] == array[2][0] and array[1][1] == "X":
            print("Blau gewinnt")
            winner_blue()
            break
        elif array[0][2] == array[1][1] and array[1][1] == array[2][0] and array[1][1] == "O":
            print("Rot gewinnt")
            winner_red()
            break

tiktaktoe.mainloop()
