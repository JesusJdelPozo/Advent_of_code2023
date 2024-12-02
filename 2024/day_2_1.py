import numpy as np


def is_safe(nb_list: np.array):
    diff = nb_list[:len(nb_list) - 1] - nb_list[1:]
    if diff[0] < 0:
        diff = -diff

    if np.all(diff > 0):
        if np.all(diff <= 3):
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    with open("input_day_2_1.txt", "r") as f:
        file = f.readlines()

    lines = [line.split("\n")[0] for line in file]
    numbers = [np.int_(np.array(n.split(" "))) for n in lines]
    safe_numbers = [np.int_(is_safe(nb)) for nb in numbers]
    print(np.sum(safe_numbers))
