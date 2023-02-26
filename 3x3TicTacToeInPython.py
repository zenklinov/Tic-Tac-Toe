from tkinter import *

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")
        
        self.current_player = "X"
        self.game_over = False
        
        self.create_board()
        self.create_reset_button()
        
    def create_board(self):
        self.board = [[None for j in range(3)] for i in range(3)]
        self.buttons = [[None for j in range(3)] for i in range(3)]
        
        for i in range(3):
            for j in range(3):
                button = Button(self.master, text="", width=4, height=2,
                                command=lambda row=i, col=j: self.handle_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button
                
    def create_reset_button(self):
        reset_button = Button(self.master, text="Reset", command=self.reset)
        reset_button.grid(row=3, column=1)
                
    def handle_click(self, row, col):
        if self.board[row][col] is None and not self.game_over:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_win(row, col):
                self.game_over = True
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
            elif self.check_draw():
                self.game_over = True
                messagebox.showinfo("Game Over", "Draw!")
            else:
                self.switch_players()
                
    def switch_players(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        
    def check_win(self, row, col):
        # Check row
        if all(cell == self.current_player for cell in self.board[row]):
            return True
        
        # Check column
        if all(self.board[i][col] == self.current_player for i in range(3)):
            return True
        
        # Check diagonal
        if row == col and all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        
        # Check anti-diagonal
        if row + col == 2 and all(self.board[i][2-i] == self.current_player for i in range(3)):
            return True
        
        return False
    
    def check_draw(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] is None:
                    return False
        return True
    
    def reset(self):
        self.current_player = "X"
        self.game_over = False
        for i in range(3):
            for j in range(3):
                self.board[i][j] = None
                self.buttons[i][j].config(text="")
        
root = Tk()
game = TicTacToe(root)
root.mainloop()
