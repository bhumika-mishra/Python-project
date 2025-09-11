import tkinter as tk
import random

def play_game_rock():
    play_game('rock')

def play_game_paper():
    play_game('paper')

def play_game_scissors():
    play_game('scissors')

def play_game(player_choice):
    choices = ['rock', 'paper', 'scissors']
    opponent_choice = random.choice(choices)

    player_choice_var.set("Your choice: " + player_choice)
    opponent_choice_var.set("Opponent's choice: " + opponent_choice)

    if player_choice == opponent_choice:
        result_var.set("It's a tie! ")
    elif (player_choice == 'rock' and opponent_choice == 'scissors') or \
         (player_choice == 'paper' and opponent_choice == 'rock') or \
         (player_choice == 'scissors' and opponent_choice == 'paper'):
        result_var.set("You win! ")
    else:
        result_var.set("Opponent wins! ")

root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x250")

player_choice_var = tk.StringVar(value="Your choice: ")
opponent_choice_var = tk.StringVar(value=" Opponent's choice: ")
result_var = tk.StringVar(value="Choose your move!")

tk.Label(root, textvariable=player_choice_var, font=("Arial", 12)).pack(pady=5)
tk.Label(root, textvariable= opponent_choice_var, font=("Arial", 12)).pack(pady=5)
tk.Label(root, textvariable=result_var, font=("Arial", 16, "bold"), fg="blue").pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Rock", width=10, command=play_game_rock).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Paper", width=10, command=play_game_paper).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Scissors", width=10, command=play_game_scissors).pack(side=tk.LEFT, padx=10)
root.mainloop()