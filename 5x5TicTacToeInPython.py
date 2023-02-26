import tkinter as tk

class TicTacToeGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.reset_button = tk.Button(self, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=0, column=0, columnspan=5)
        self.turn_label = tk.Label(self, text="Player X's turn")
        self.turn_label.grid(row=1, column=0, columnspan=5)
        self.buttons = []
        for row in range(5):
            for col in range(5):
                button = tk.Button(self, text="", width=3, height=1, command=lambda row=row, col=col: self.button_click(row, col))
                button.grid(row=row+2, column=col)
                self.buttons.append(button)
        self.game_over = False
        self.current_player = "X"

    def button_click(self, row, col):
        if not self.game_over:
            button = self.buttons[row*5+col]
            if button["text"] == "":
                button["text"] = self.current_player
                if self.check_win(row, col):
                    self.turn_label["text"] = f"Player {self.current_player} wins!"
                    self.game_over = True
                elif self.check_draw():
                    self.turn_label["text"] = "Draw!"
                    self.game_over = True
                else:
                    self.switch_turn()

    def check_win(self, row, col):
        for i in range(5):
            if self.buttons[row*5+i]["text"] != self.current_player:
                break
        else:
            return True
        for i in range(5):
            if self.buttons[i*5+col]["text"] != self.current_player:
                break
        else:
            return True
        if row == col:
            for i in range(5):
                if self.buttons[i*5+i]["text"] != self.current_player:
                    break
            else:
                return True
        if row == 4 - col:
            for i in range(5):
                if self.buttons[i*5+4-i]["text"] != self.current_player:
                    break
            else:
                return True
        return False

    def check_draw(self):
        for button in self.buttons:
            if button["text"] == "":
                return False
        return True

    def switch_turn(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.turn_label["text"] = f"Player {self.current_player}'s turn"

    def reset_game(self):
        for button in self.buttons:
            button["text"] = ""
        self.game_over = False
        self.current_player = "X"
        self.turn_label["text"] = "Player X's turn"

root = tk.Tk()
root.title("Tic Tac Toe")
app = TicTacToeGUI(master=root)
app.mainloop()
