# Tic-Tac-Toe with Minimax
This is a simple Tic-Tac-Toe game implemented in Python with Tkinter for the GUI. It uses the minimax algorithm to allow the computer (player X) to play optimally and never lose.

### How to Play
Clone the repo and run python tictactoe.py to start the game
You are player O and make the first move by clicking on any empty square
The computer (X) will then make the optimal move
Take turns until someone wins or there is a draw

### Rules
X always goes first
Players cannot play on squares that are already occupied
The first player to get 3 of their marks in a row (horizontally, vertically or diagonally) wins
If all 9 squares are occupied and no one has won, the game is a draw

### Minimax Algorithm
The minimax algorithm is used to allow the computer (X) to play optimally. It works by looking ahead at all possible moves and outcomes, then choosing the move that maximizes its chance of winning.

The pseudo-code is:

```
function minimax(board, isMaximizing)
  if terminal state
    return value of state
  
  if isMaximizing
    bestVal = -infinity 
    for each child node
      v = minimax(child, FALSE) 
      bestVal = max(bestVal, v)
    return bestVal
    
  else 
    bestVal = +infinity
    for each child node
      v = minimax(child, TRUE)
      bestVal = min(bestVal, v) 
    return bestVal
```

At each move, it looks at available moves, plays them out recursively to establish scores, and then chooses the move that maximizes its own score.

This allows it to play perfectly without losing (unless the player gets lucky and forces a draw).

###To Do
Some ideas for improvements:

- Let the user choose to go first or second
- Add graphics and animations for a better UI
- Allow custom board sizes (e.g. 4x4)
- Allow the computer to play against itself
- Implement alpha-beta pruning for faster performance

License
This project is open source and available under the MIT License.
