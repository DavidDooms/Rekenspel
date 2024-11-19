import numpy as np
import tkinter as tk
import tkinter.ttk as tkk

end_game = False

window = tk.Tk()
window.geometry("100x100")

greeting = tk.Label(text="HALLO ROXANE! \n\n WE GAAN REKENEN!", bg="pink")
greeting.pack()

start_button = tk.Button(window, text="START", command=window.destroy)
start_button.pack(padx=5, pady=10)

window = tk.Tk()
window.geometry("100x100")

window.mainloop()

while not end_game:
    num1 = np.random.randint(11)
    num2 = np.random.randint(11)

    sol = input(f"Hoeveel is {num1} + {num2}? Stoppen? (Q)")

    if sol.lower() == "q":
        end_game = True
        print("Einde spelletje, goed gedaan!")
    else:
        while not (int(sol) == (num1 + num2)):
            print(f"Fout, probeer opnieuw!")
            sol = input(f"Hoeveel is {num1} + {num2}?")

    print("Goed bezig!")


