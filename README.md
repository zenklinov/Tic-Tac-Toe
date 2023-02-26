# Tic Tac Toe
Tic Tac Toe, also known as noughts and crosses or Xs and Os, is a popular two-player strategy game played on a 3x3 grid. The game is typically played with Xs and Os, with the first player placing X in an empty square, followed by the second player placing O in a different empty square, and so on.

The objective of the game is for a player to place three of their marks in a horizontal, vertical, or diagonal row on the grid, while preventing their opponent from doing the same. The game ends in a draw if all nine squares are filled without either player achieving a winning position.

Tic Tac Toe is often used as a teaching tool to introduce young children to the concepts of strategy, planning, and critical thinking. It is a simple and fun game that can be played virtually anywhere with nothing more than a piece of paper and a pen or pencil.

Here is an example code: 
1. 3x3 grid, copy the code from [3x3TicTacToeInPython.py](https://github.com/zenklinov/Tic-Tac-Toe/blob/main/3x3TicTacToeInPython.py)
2. 5x5 grid, copy the code from [5x5TicTacToeInPython.py](https://github.com/zenklinov/Tic-Tac-Toe/blob/main/5x5TicTacToeInPython.py)

In this implementation, we use a nested list to represent the game board, where each element is initially set to None. We use the ```create_board()``` method to create a 5x5 grid of buttons in the GUI, and the ```handle_click()``` method to handle clicks on the buttons. The ```check_win()``` method checks if the current player has won the game, and the ```check_draw()``` method checks if the game has ended in a draw. Finally, the ```reset()``` method resets the game board and GUI to their initial state.

To run the game, simply run the code in a Python environment that has Tkinter installed, and a GUI window will appear with the game board and reset button. Clicking on a button will place the current player's mark (X or O) in the corresponding square, and the game will continue until one player wins or the game ends in a draw. Clicking the reset button will reset the game board and allow for a new game to be played.

*Note that this implementation uses the ```messagebox``` module from Tkinter to display the winner or draw message in a pop-up window. You can import it by adding the following line at the top of the file:

```from tkinter import messagebox```

Additionally, this implementation does not have any specific design, but you can customize the GUI by changing the font, colors, or layout of the game board and reset button.
