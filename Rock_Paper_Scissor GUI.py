import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.title("Rock Paper Scissor Game")
root.minsize(250, 250)

def rock_checking():
    lst = ['rock', 'paper', 'scissor']
    rock_guess = str(lst[0])
    computer_guess = random.randint(0, 2)
    counter = 0
    while True:
        if rock_guess == str(lst[0]):
            if computer_guess == 1:
                tk.messagebox.showinfo('Game', 'Computer Guess: Paper\n\nOooops!!! You Are A Loser')
                break
            elif computer_guess == 2:
                tk.messagebox.showinfo('Game', 'Computer Guess: Scissor\n\nCongrates!!! You Won')
                break
            elif computer_guess == 0:
                if counter > 0:
                    break
                counter = counter + 1
                tk.messagebox.showinfo('Game', 'Computer Guess: Rock\n\nITS A TIE')
                continue


def paper_checking():
    lst = ['rock', 'paper', 'scissor']
    paper_guess = str(lst[1])
    computer_guess = random.randint(0, 2)
    counter = 0
    while True:
        if paper_guess == str(lst[1]):
            if computer_guess == 1:
                if counter > 0:
                    break
                counter = counter + 1
                tk.messagebox.showinfo('Game', 'Computer Guess: Paper\n\nITS A TIE')
                continue
            elif computer_guess == 0:
                tk.messagebox.showinfo('Game', 'Computer Guess: Rock\n\nCongrates!!! You Won')
                break
            elif computer_guess == 2:
                tk.messagebox.showinfo('Game', 'Computer Guess: Scissor\n\nOooops!!! You Are A Loser')
                break


def scissor_checking():
    lst = ['rock', 'paper', 'scissor']
    scissor_guess = str(lst[2])
    computer_guess = random.randint(0, 2)
    counter = 0
    while True:
        if scissor_guess == str(lst[2]):
            if counter > 0:
                break
            counter = counter + 1
            if computer_guess == 2:
                tk.messagebox.showinfo('Game', 'Computer Guess: Scissor\n\nITS A TIE')
                continue
            elif computer_guess == 0:
                tk.messagebox.showinfo('Game', 'Computer Guess: Rock\n\nOooops You Are A Loser')
                break
            elif computer_guess == 1:
                tk.messagebox.showinfo('Game', 'Computer Guess: Paper\n\nCongrates!!! You Won')
                break


# Labels
choice_label = tk.Label(root, text='Select Your Guess Below', fg='black' , font=('Times', 16))
choice_label.pack(padx=5, pady=5)
# Buttons
rock_button = tk.Button(root, text='Rock', font=('Times', 16, 'bold'),
                        bd=3, fg='white', bg='red', command=rock_checking)
rock_button.pack(fill='x', padx=10, pady=10)
paper_button = tk.Button(root, text='Paper', font=('Times', 16, 'bold'),
                         bd=3, fg='white', bg='red', command=paper_checking)
paper_button.pack(fill='x', padx=10, pady=10)
scissor_button = tk.Button(root, text='Scissor', font=('Times', 16, 'bold'),
                           bd=3, fg='white', bg='red', command=scissor_checking)
scissor_button.pack(fill='x', padx=10, pady=10)

root.mainloop()
