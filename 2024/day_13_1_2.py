import numpy as np


def int_division(a, b):
    v = abs(int(a / b) - a / b)
    if np.allclose(v, 0, rtol=1.e-3, atol=1.e-3):
        return int(a / b)

    elif np.allclose(v, 1, rtol=1.e-3, atol=1.e-3):
        return int(a / b) + 1

    else:
        return 0


def check_answer(nb_a, nb_b, button_a, button_b, prize):
    if nb_a > 100 and nb_b > 100:  # Comment this if statement for part 2
        nb_a, nb_b = 0, 0

    cond_1 = nb_a * button_a[0] + nb_b * button_b[0] == prize[0]
    cond_2 = nb_a * button_a[1] + nb_b * button_b[1] == prize[1]
    return cond_1 and cond_2


if __name__ == '__main__':
    with open("input_day_13.txt", "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines if line != ""]
    added_quantity = 10000000000000 # Set the added constant for part 2
    button_a = [(int(line.split("+")[1].split(",")[0]), int(line.split("+")[-1])) for line in lines[::4] if line != ""]
    button_b = [(int(line.split("+")[1].split(",")[0]), int(line.split("+")[-1])) for line in lines[1::4] if line != ""]
    prize = [(int(line.split("=")[1].split(",")[0]) + added_quantity, int(line.split("=")[-1]) + added_quantity) for
             line in lines[2::4] if line != ""]
    total_tokens = 0
    for i in range(len(button_a)):
        div = button_a[i][0] - button_a[i][1] * button_b[i][0] / button_b[i][1]
        if div != 0:
            div2 = prize[i][0] - prize[i][1] * button_b[i][0] / button_b[i][1]
            nb_a = int_division(div2, div)
            nb_b = int_division((prize[i][1] - nb_a * button_a[i][1]), button_b[i][1])
            if check_answer(nb_a, nb_b, button_a[i], button_b[i], prize[i]):
                tokens = 3 * nb_a + nb_b
                total_tokens += tokens

    print(total_tokens)

