from src.engine import MathGame

import numpy as np
import tkinter as tk
import tkinter.ttk as tkk


def submit():
    answer.get()
    answer.set("")


end_game = True

while not end_game:
    num1 = np.random.randint(11)
    num2 = np.random.randint(11)

    answer = tk.StringVar()

    question = tk.Label(text=f"Hoeveel is {num1} + {num2}?")
    question.pack()
    solution = tk.Entry(textvariable=answer, fg="yellow", bg="blue", width=50)
    solution.pack()

    sol = solution.get()

    submit_button = tk.Button(text="OK", command=submit)
    submit_button.pack()

    if sol.lower() == "q":
        end_game = True
        end = tk.Label(text="Einde spelletje, goed gedaan!")
        end.pack()
    else:
        cont = tk.Label(text="Goed bezig!")
        cont.pack()

        """while not (int(sol) == (num1 + num2)):
            tk.Label(text="Fout, probeer opnieuw!")
            sol = input(f"Hoeveel is {num1} + {num2}?")"""


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("200x200")
    window.configure(background="pink")

    greeting = tk.Label(text="HALLO ROXANE! \n\n WE GAAN REKENEN!", bg="pink")
    greeting.pack()

    start_button = tk.Button(window, text="START", command=window.destroy)
    start_button.pack(padx=5, pady=10)

    window.mainloop()

    window = tk.Tk()
    window.geometry("200x200")
    window.configure(background="pink")
    
    game = MathGame(window)
    window.mainloop()
