import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    
    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def player_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Please enter valid numbers for row and column.")

def computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        
        if board[row][col] == " ":
            board[row][col] = "O"
            print(f"Computer places O at ({row}, {col})")
            break

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    while True:
        print_board(board)
        
        # Player move
        print("Your turn (X)")
        player_move(board)
        
        # Check for winner or full board after player's move
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Computer move
        print("Computer's turn (O)")
        computer_move(board)
        
        # Check for winner or full board after computer's move
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    tic_tac_toe()
