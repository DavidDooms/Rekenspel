import tkinter as tk
import numpy as np


class MathGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Math Game")

        # Initialize game state
        self.num1 = 0
        self.num2 = 0
        self.solution = 0

        self.total_games = 0
        self.score = 0

        self.end_game = False

        # GUI Elements
        self.question_label = tk.Label(self.master, text="Press 'Start' to begin")
        self.question_label.pack()

        self.answer_entry = tk.Entry(self.master)
        self.answer_entry.pack()

        self.feedback_label = tk.Label(self.master, text="")
        self.feedback_label.pack()

        self.score_label = tk.Label(self.master, text=f"{self.score} / {self.total_games}")
        self.score_label.pack()

        self.start_button = tk.Button(self.master, text="Start", command=self.start_game)
        self.start_button.pack()

        self.submit_button = tk.Button(self.master, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack()

        self.quit_button = tk.Button(self.master, text="Quit", command=self.quit_game)
        self.quit_button.pack()

    def start_game(self):
        """Start a new game by generating the first question."""
        self.end_game = False
        self.ask_question()

    def ask_question(self):
        """Generate a new question and display it."""
        self.num1 = np.random.randint(11)
        self.num2 = np.random.randint(11)
        self.solution = self.num1 + self.num2

        self.total_games += 1

        self.question_label.config(text=f"Hoeveel is {self.num1} + {self.num2}?")
        self.answer_entry.delete(0, tk.END)  # Clear any previous answer
        self.feedback_label.config(text="")

    def check_answer(self):
        """Check the user's answer."""
        if self.end_game:
            return

        user_answer = self.answer_entry.get()

        if user_answer.lower() == 'q':
            self.quit_game()
            return

        try:
            user_answer = int(user_answer)
            if user_answer == self.solution:
                self.feedback_label.config(text="Goed zo!")
                self.score += 1
                self.score_label.config(text=f"{self.score} / {self.total_games}")
                self.ask_question()  # Move to the next question
            else:
                self.feedback_label.config(text="Fout, probeer opnieuw!")
                self.score_label.config(text=f"{self.score} / {self.total_games}")
                self.total_games += 1
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.")

    def quit_game(self):
        """End the game."""
        self.end_game = True
        self.question_label.config(text="Einde spelletje, goed gedaan!")
        self.answer_entry.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    game = MathGame(root)
    root.mainloop()
