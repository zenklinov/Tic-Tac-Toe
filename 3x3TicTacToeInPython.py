import tkinter as tk
from tkinter import messagebox

# Set up the game board
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 'X'

# Define the function to reset the game
def reset_game():
    global board, player
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player = 'X'
    for i in range(9):
        labels[i].config(text=board[i])
    status_label.config(text=f"Player {player}'s turn")

# Define the function to handle a player's move
def player_move(cell):
    global player
    if board[cell] == ' ':
        board[cell] = player
        labels[cell].config(text=player)
        # Check for a win or tie
        if (board[0] == board[1] == board[2] != ' ' or
            board[3] == board[4] == board[5] != ' ' or
            board[6] == board[7] == board[8] != ' ' or
            board[0] == board[3] == board[6] != ' ' or
            board[1] == board[4] == board[7] != ' ' or
            board[2] == board[5] == board[8] != ' ' or
            board[0] == board[4] == board[8] != ' ' or
            board[2] == board[4] == board[6] != ' '):
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_game()
        elif ' ' not in board:
            messagebox.showinfo("Game Over", "Tie game!")
            reset_game()
        # Switch to the other player's turn
        player = 'O' if player == 'X' else 'X'
        status_label.config(text=f"Player {player}'s turn")

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create the labels for each cell on the board
labels = []
for i in range(3):
    for j in range(3):
        label = tk.Label(root, text=board[i*3+j], font=('Arial', 60), width=3, height=1, relief='groove')
        label.grid(row=i, column=j)
        labels.append(label)

# Create the "Reset" button
reset_button = tk.Button(root, text="Reset", font=('Arial', 20), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Create the status label
status_label = tk.Label(root, text=f"Player {player}'s turn", font=('Arial', 20))
status_label.grid(row=4, column=0, columnspan=3)

# Bind each label to the player's move function
for i in range(9):
    labels[i].bind("<Button-1>", lambda event, i=i: player_move(i))

# Start the game
root.mainloop()

import tkinter as tk
from tkinter import messagebox


class GameState:
    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.current_player = 'X'


def handle_cell_click(game_state, cell):
    if game_state.board[cell] == ' ':
        game_state.board[cell] = game_state.current_player
        labels[cell].config(text=game_state.current_player)
        # Check for a win or tie
        if (game_state.board[0] == game_state.board[1] == game_state.board[2] != ' ' or
            game_state.board[3] == game_state.board[4] == game_state.board[5] != ' ' or
            game_state.board[6] == game_state.board[7] == game_state.board[8] != ' ' or
            game_state.board[0] == game_state.board[3] == game_state.board[6] != ' ' or
            game_state.board[1] == game_state.board[4] == game_state.board[7] != ' ' or
            game_state.board[2] == game_state.board[5] == game_state.board[8] != ' ' or
            game_state.board[0] == game_state.board[4] == game_state.board[8] != ' ' or
            game_state.board[2] == game_state.board[4] == game_state.board[6] != ' '):
            messagebox.showinfo("Game Over", f"Player {game_state.current_player} wins!")
            reset_game(game_state)
        elif ' ' not in game_state.board:
            messagebox.showinfo("Game Over", "Tie game!")
            reset_game(game_state)
        # Switch to the other player's turn
        game_state.current_player = 'O' if game_state.current_player == 'X' else 'X'
        status_label.config(text=f"Player {game_state.current_player}'s turn")


def reset_game(game_state):
    game_state.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    game_state.current_player = 'X'
    for i in range(9):
        labels[i].config(text=game_state.board[i])
    status_label.config(text=f"Player {game_state.current_player}'s turn")
