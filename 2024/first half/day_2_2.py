import numpy as np
from day_2_1 import is_safe


def is_safe_2(nb_list: np.array):
    # Brute force it.
    # If we try with all the arrays missing one element and don't found one that is safe then it is not safe
    for i in range(len(nb_list)):
        new_list = np.delete(nb_list, i)
        if is_safe(new_list):
            return True

    return False


if __name__ == '__main__':
    with open("input_day_2_1.txt", "r") as f:
        file = f.readlines()

    lines = [line.split("\n")[0] for line in file]
    numbers = [np.int_(np.array(n.split(" "))) for n in lines]
    safe_numbers = np.array([np.int_(is_safe_2(nb)) for nb in numbers])
    print(np.sum(safe_numbers))
