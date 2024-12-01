import numpy as np


if __name__ == '__main__':
    with open("input_day_1_1.txt", "r") as f:
        lines = f.readlines()

    numbers = [line.split("\n")[0] for line in lines]
    left = np.array([int(number.split("  ")[0]) for number in numbers])
    right = np.array([int(number.split("  ")[1]) for number in numbers])

    left_sorted = np.sort(left)
    right_sorted = np.sort(right)
    difference = np.abs(right_sorted - left_sorted)
    print(np.sum(difference))
