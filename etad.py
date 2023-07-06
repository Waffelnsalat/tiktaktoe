#imports
import tkinter
from tkinter import *

tiktaktoe =Tk()

tiktaktoe.geometry("300x300")
tiktaktoe.title("TikTakToe")

tiktaktoe.rowconfigure([0, 1, 2], minsize=90, weight=1)
tiktaktoe.columnconfigure([0, 1, 2], minsize=90, weight=1)

def player(row, column):
    round = 0
    if round % 2 == 0:
        btn_one = tkinter.Button(master=tiktaktoe, text="X", font=('times', 35, 'bold'), foreground="blue")
        btn_one.grid(row=row, column=column, sticky="nsew")
    elif round % 2 == 1:
        btn_one = tkinter.Button(master=tiktaktoe, text="O", font=('times', 35, 'bold'), foreground="red")
        btn_one.grid(row=0, column=0, sticky="nsew")


for row in range(3):
    for column in range(3):
        btn_one = tkinter.Button(master=tiktaktoe, text="", command=player, font=('times', 35, 'bold'))
        btn_one.grid(row=str(row), column=str(range), sticky="nsew")


btn_one = tkinter.Button(master=tiktaktoe, text="", command= player, font=('times', 35, 'bold'))
btn_one.grid(row=0, column=0, sticky="nsew")

btn_two = tkinter.Button(master=tiktaktoe, text="", font=('times', 35, 'bold'))
btn_two.grid(row=1, column=0, sticky="nsew")

btn_three = tkinter.Button(master=tiktaktoe, text="", font=('times', 35, 'bold'))
btn_three.grid(row=2, column=0, sticky="nsew")

btn_four = tkinter.Button(master=tiktaktoe, text="", font=('times', 35, 'bold'))
btn_four.grid(row=0, column=1, sticky="nsew")

btn_five = tkinter.Button(master=tiktaktoe, text="", font=('times', 35, 'bold'))
btn_five.grid(row=1, column=1, sticky="nsew")

btn_six = tkinter.Button(master=tiktaktoe, text="", font=('times', 35, 'bold'))
btn_six.grid(row=2, column=1, sticky="nsew")

btn_seven = tkinter.Button(master=tiktaktoe, text="", font=('times', 35, 'bold'))
btn_seven.grid(row=0, column=2, sticky="nsew")

btn_eight = tkinter.Button(master=tiktaktoe, text="", font=('times', 35, 'bold'))
btn_eight.grid(row=1, column=2, sticky="nsew")

btn_nine = tkinter.Button(master=tiktaktoe, text="", font=('times', 35, 'bold'))
btn_nine.grid(row=2, column=2, sticky="nsew")

tiktaktoe.mainloop()
