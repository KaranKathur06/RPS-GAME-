import tkinter as tk
from tkinter import messagebox
import random

# Function to get the COMPUTER's choice
def get_COMPUTER_choice():
    choices = ['ROCK', 'PAPER', 'SCISSOR']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(USER_choice, COMPUTER_choice):
    if USER_choice == COMPUTER_choice:
        return 'TIE'
    elif (USER_choice == 'ROCK' and COMPUTER_choice == 'SCISSOR') or \
         (USER_choice == 'PAPER' and COMPUTER_choice == 'ROCK') or \
         (USER_choice == 'SCISSOR' and COMPUTER_choice == 'PAPER'):
        return 'USER'
    else:
        return 'COMPUTER'

# Function to play a round
def play_round(USER_choice):
    COMPUTER_choice = get_COMPUTER_choice()
    winner = determine_winner(USER_choice, COMPUTER_choice)

    if winner == 'USER':
        result.set(f"YOU: {USER_choice}, COMPUTER: {COMPUTER_choice}. \n CONGO, YOU BEAT THE COMPUTER <3")
        scores['USER'] += 1
    elif winner == 'COMPUTER':
        result.set(f"YOU: {USER_choice}, COMPUTER : {COMPUTER_choice}. \n COMPUTER JUST CRASHED YOU SAD :(")
        scores['COMPUTER'] += 1
    else:
        result.set(f"YOU: {USER_choice}, COMPUTER : {COMPUTER_choice}.\n HOHOHO IT'S A TIE CAN'T WIN TO COMPUTER :)")
        scores['ties'] += 1

    update_scoreboard()

# Function to update the scoreboard
def update_scoreboard():
    USER_score.set(f"USER: {scores['USER']}")
    COMPUTER_score.set(f"COMPUTER: {scores['COMPUTER']}")
    ties_score.set(f"Ties: {scores['ties']}")

# Initialize scores
scores = {'USER': 0, 'COMPUTER': 0, 'ties': 0}

# Create the main window
root = tk.Tk()
root.title("ROCK-PAPER-SCISSOR Game")

# Create a frame for the buttons
frame = tk.Frame(root)
frame.pack(pady=20)

# Create buttons for ROCK, PAPER, and SCISSOR
ROCK_button = tk.Button(frame, text="ROCK", command=lambda: play_round('ROCK'))
ROCK_button.grid(row=0, column=0, padx=10)

PAPER_button = tk.Button(frame, text="PAPER", command=lambda: play_round('PAPER'))
PAPER_button.grid(row=0, column=1, padx=10)

SCISSOR_button = tk.Button(frame, text="SCISSOR", command=lambda: play_round('SCISSOR'))
SCISSOR_button.grid(row=0, column=2, padx=10)

# Create a label to display the result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=('Helvetica', 14))
result_label.pack(pady=20)

# Create labels to display the scores
USER_score = tk.StringVar()
COMPUTER_score = tk.StringVar()
ties_score = tk.StringVar()

USER_score_label = tk.Label(root, textvariable=USER_score)
USER_score_label.pack()

COMPUTER_score_label = tk.Label(root, textvariable=COMPUTER_score)
COMPUTER_score_label.pack()

ties_score_label = tk.Label(root, textvariable=ties_score)
ties_score_label.pack()

# Initialize the scoreboard
update_scoreboard()

# Run the main loop
root.mainloop()
