import tkinter as tk
from tkinter import messagebox

# Define the symbols for the players
X = "X"
O = "O"
EMPTY = " "

# Define the utility values for terminal states
WIN = 1
DRAW = 0
LOSS = -1

# Initialize the board
board = [EMPTY for _ in range(9)]

# Create a root window
root = tk.Tk()

# Define a function to check if a player has won
def is_win(symbol):
    # Check horizontal lines
    if board[0] == board[1] == board[2] == symbol:
        return True
    if board[3] == board[4] == board[5] == symbol:
        return True
    if board[6] == board[7] == board[8] == symbol:
        return True
    # Check vertical lines
    if board[0] == board[3] == board[6] == symbol:
        return True
    if board[1] == board[4] == board[7] == symbol:
        return True
    if board[2] == board[5] == board[8] == symbol:
        return True
    # Check diagonal lines
    if board[0] == board[4] == board[8] == symbol:
        return True
    if board[2] == board[4] == board[6] == symbol:
        return True
    # Otherwise, no win
    return False

# Define a function to check if the board is full
def is_full():
    return EMPTY not in board
    
# Define a function to evaluate the utility value of a terminal state
def evaluate():
    # If X wins, return WIN
    if is_win(X):
        return WIN
    # If O wins, return LOSS
    if is_win(O):
        return LOSS
    # If draw, return DRAW
    if is_full():
        return DRAW

# Define a function to implement the minimax algorithm
def minimax(is_maximizing):
    # If the game is over, return the utility value
    if is_win(X) or is_win(O) or is_full():
        return evaluate()
    # If the player is maximizing, initialize the best value to negative infinity and loop through all the possible moves
    if is_maximizing:
        best_value = -float("inf")
        for i in range(9):
            # If the cell is empty, make the move and recursively call minimax for the minimizing player
            if board[i] == EMPTY:
                board[i] = X
                value = minimax(False)
                # Undo the move and update the best value if needed
                board[i] = EMPTY
                best_value = max(best_value, value)
        # Return the best value for the maximizing player
        return best_value
    # If the player is minimizing, initialize the best value to positive infinity and loop through all the possible moves
    else:
        best_value = float("inf")
        for i in range(9):
            # If the cell is empty, make the move and recursively call minimax for the maximizing player
            if board[i] == EMPTY:
                board[i] = O
                value = minimax(True)
                # Undo the move and update the best value if needed
                board[i] = EMPTY
                best_value = min(best_value, value)
        # Return the best value for the minimizing player
        return best_value

# Define a function to find the best move for the computer (X)
def find_best_move():
    # Initialize the best value to negative infinity and the best move to -1
    best_value = -float("inf")
    best_move = -1
    # Loop through all the possible moves
    for i in range(9):
        # If the cell is empty, make the move and call minimax for the minimizing player
        if board[i] == EMPTY:
            board[i] = X
            value = minimax(False)
            # Undo the move and update the best value and move if needed
            board[i] = EMPTY
            if value > best_value:
                best_value = value
                best_move = i
    # Return the best move for the computer
    return best_move

# Define a function to handle user input (O)
def make_user_move(i):
    if board[i] == EMPTY:
        board[i] = O
        buttons[i].config(text=O)
        if is_win(O):
            messagebox.showinfo("Game over", "You win!")
            root.destroy()  # Destroy the root window
        elif is_full() and not is_win(X):  # If the board is full and X has not won
            messagebox.showinfo("Game over", "It's a draw!")
            root.destroy()
        else:
            make_computer_move()

# Define a function to handle computer input (X)
def make_computer_move():
    if not is_full():
        move = find_best_move()
        board[move] = X
        buttons[move].config(text=X)
        if is_win(X):
            messagebox.showinfo("Game over", "Computer wins!")
            root.destroy()  # Destroy the root window
        elif is_full() and not is_win(O):  # If the board is full and O has not won
            messagebox.showinfo("Game over", "It's a draw!")
            root.destroy()

# Create buttons for the board
buttons = []
for i in range(9):
    button = tk.Button(root, text=EMPTY, command=lambda i=i: make_user_move(i), width=10, height=3, font=('Helvetica', '20'))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Start the tkinter main loop
root.mainloop()

