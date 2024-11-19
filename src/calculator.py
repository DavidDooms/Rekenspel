import numpy as np

end_game = False

while not end_game:
    num1 = np.random.randint(11)
    num2 = np.random.randint(11)

    solution = input(f"Hoeveel is {num1} + {num2}? Stoppen? (Q)")

    if solution.lower() == "q":
        end_game = True
        print("Einde spelletje, goed gedaan!")
    else:
        while not (int(solution) == (num1 + num2)):
            print(f"Fout, probeer opnieuw!")
            sol = input(f"Hoeveel is {num1} + {num2}?")

    print("Goed bezig!")