import tkinter as tk
from tkinter import messagebox
import random
import math

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.configure(bg="#F0F0F0")  # Light background color for the window

# Global variables for the game
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

# Functions to check the game state
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_board_full():
    for row in board:
        if " " in row:
            return False
    return True

# Function for player move
def player_move(row, col):
    global current_player
    if board[row][col] == " " and current_player == "X":
        board[row][col] = "X"
        buttons[row][col].config(text="X", state=tk.DISABLED, disabledforeground="#007BFF")
        current_player = "O"
        check_game_state()

        # After player move, let the computer move
        root.after(500, computer_move)

# Function for computer move (with Minimax)
def computer_move():
    global current_player
    if current_player == "O":
        best_score = -math.inf
        best_move = None

        # Try all possible moves and pick the best one using Minimax
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = minimax(board, 0, False)
                    board[row][col] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        if best_move:
            row, col = best_move
            board[row][col] = "O"
            buttons[row][col].config(text="O", state=tk.DISABLED, disabledforeground="#FF4136")
            current_player = "X"
            check_game_state()

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner()
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_board_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = minimax(board, depth + 1, False)
                    board[row][col] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    score = minimax(board, depth + 1, True)
                    board[row][col] = " "
                    best_score = min(score, best_score)
        return best_score

# Function to check for a winner or tie
def check_game_state():
    winner = check_winner()
    if winner:
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        reset_board()
    elif is_board_full():
        messagebox.showinfo("Game Over", "It's a tie!")
        reset_board()

# Function to reset the board
def reset_board():
    global board, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ", state=tk.NORMAL, bg="#FFFFFF")

# Create a style for buttons
button_style = {
    "font": ('Arial', 40),
    "bg": "#FFFFFF",
    "activebackground": "#E0E0E0",
    "relief": tk.FLAT,
    "highlightthickness": 0,
}

# Create buttons for the grid
buttons = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        btn = tk.Button(root, text=" ", width=5, height=2, command=lambda r=row, c=col: player_move(r, c), **button_style)
        btn.grid(row=row, column=col, padx=10, pady=10)
        buttons[row][col] = btn  # Store the button in the buttons array

# Start the Tkinter main loop
root.mainloop()
