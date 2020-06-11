import tkinter as tk
from tkinter import messagebox

button_param = {"height": 4, "width": 4,
                "font": "Times 15 bold", "activebackground": "gray74"}


class TicTacToe(tk.Frame):
    def __init__(self, master=None):
        """
        Construct a frame widget with the parent MASTER for the class TicTacToe.
        
        """
        tk.Frame.__init__(self, master)
        self.grid()
        self.master.resizable(width=False, height=False)
        self.master.title("Tic-Tac-Toe")
        self.flag = True
        self.num_x = 0
        self.num_o = 0
        self.create_widgets()
        self.mainloop()

    def create_widgets(self):
        self.but1 = tk.Button(self, **button_param,
                              command=lambda: self.click(self.but1))
        self.but1.grid(row=0, column=0)
        self.but2 = tk.Button(self, **button_param,
                              command=lambda: self.click(self.but2))
        self.but2.grid(row=0, column=1)
        self.but3 = tk.Button(self, **button_param,
                              command=lambda: self.click(self.but3))
        self.but3.grid(row=0, column=2)
        self.but4 = tk.Button(self, **button_param,
                              command=lambda: self.click(self.but4))
        self.but4.grid(row=1, column=0)
        self.but5 = tk.Button(self, **button_param,
                              command=lambda: self.click(self.but5))
        self.but5.grid(row=1, column=1)
        self.but6 = tk.Button(self, **button_param,
                              command=lambda: self.click(self.but6))
        self.but6.grid(row=1, column=2)
        self.but7 = tk.Button(self, **button_param,
                              command=lambda: self.click(self.but7))
        self.but7.grid(row=2, column=0)
        self.but8 = tk.Button(self, **button_param,
                              command=lambda: self.click(self.but8))
        self.but8.grid(row=2, column=1)
        self.but9 = tk.Button(self, **button_param,
                              command=lambda: self.click(self.but9))
        self.but9.grid(row=2, column=2)

    def click(self, button):
        if self.flag == True:
            button.configure(text="X")
            self.num_x += 1
            self.flag = False
            self.winner()
        else:
            button.configure(text="O")
            self.num_o += 1
            self.flag = True
            self.winner()
        if button["text"] == "X" or button["text"] == "O":
            button.configure(state="disabled")

    def winner(self):
        if (self.but1["text"] == "X" and self.but2["text"] == "X" and self.but3["text"] == "X" or
            self.but4["text"] == "X" and self.but5["text"] == "X" and self.but6["text"] == "X" or
            self.but7["text"] == "X" and self.but8["text"] == "X" and self.but9["text"] == "X" or
            self.but1["text"] == "X" and self.but5["text"] == "X" and self.but9["text"] == "X" or
            self.but3["text"] == "X" and self.but5["text"] == "X" and self.but7["text"] == "X" or
            self.but1["text"] == "X" and self.but4["text"] == "X" and self.but7["text"] == "X" or
            self.but2["text"] == "X" and self.but5["text"] == "X" and self.but8["text"] == "X" or
                self.but3["text"] == "X" and self.but6["text"] == "X" and self.but9["text"] == "X"):
            tk.messagebox.showinfo(title="Winner", message="X won!")
            conf = tk.messagebox.askquestion(
                message="Do you want to play again?")
            if conf == "yes":
                self.play_again()
            else:
                self.master.destroy()
        elif (self.but1["text"] == "O" and self.but2["text"] == "O" and self.but3["text"] == "O" or
              self.but4["text"] == "O" and self.but5["text"] == "O" and self.but6["text"] == "O" or
              self.but7["text"] == "O" and self.but8["text"] == "O" and self.but9["text"] == "O" or
              self.but1["text"] == "O" and self.but5["text"] == "O" and self.but9["text"] == "O" or
              self.but3["text"] == "O" and self.but5["text"] == "O" and self.but7["text"] == "O" or
              self.but1["text"] == "O" and self.but4["text"] == "O" and self.but7["text"] == "O" or
              self.but2["text"] == "O" and self.but5["text"] == "O" and self.but8["text"] == "O" or
              self.but3["text"] == "O" and self.but6["text"] == "O" and self.but9["text"] == "O"):
            tk.messagebox.showinfo(title="Winner", message="O won!")
            conf = tk.messagebox.askquestion(
                message="Do you want to play again?")
            if conf == "yes":
                self.play_again()
            else:
                self.master.destroy()
        else:
            if self.num_x == 5 and self.num_o == 4:
                tk.messagebox.showinfo(message="It\'s a tie game!")
                conf = tk.messagebox.askquestion(
                    message="Do you want to play again?")
                if conf == "yes":
                    self.play_again()
                else:
                    self.master.destroy()

    def play_again(self):
        self.num_x = 0
        self.num_o = 0
        self.flag = True
        self.create_widgets()


def main():
    TicTacToe()


if __name__ == "__main__":
    main()
