import numpy as np
import tkinter as tk
import tkinter.ttk as tkk

window = tk.Tk()
window.geometry("1000x1000")

greeting = tk.Label(text="HALLO ROXANE! \n\n WE GAAN REKENEN!", bg="pink")
greeting.pack()

start_button = tk.Button(window, text="START", command=window.destroy)
start_button.pack(padx=5, pady=10)

window.mainloop()

window = tk.Tk()
window.geometry("1000x1000")

#window.mainloop()

end_game = False

while not end_game:
    num1 = np.random.randint(11)
    num2 = np.random.randint(11)

    question = tk.Label(text=f"Hoeveel is {num1} + {num2}?")
    solution = tk.Entry(fg="yellow", bg="blue", width=50)
    #sol = input(f"Hoeveel is {num1} + {num2}? Stoppen? (Q)")

    window.mainloop()
    if solution.lower() == "q":
        end_game = True
        print("Einde spelletje, goed gedaan!")
    else:
        while not (int(solution) == (num1 + num2)):
            print(f"Fout, probeer opnieuw!")
            sol = input(f"Hoeveel is {num1} + {num2}?")

    print("Goed bezig!")


