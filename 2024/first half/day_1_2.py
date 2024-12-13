import numpy as np


if __name__ == '__main__':
    with open("input_day_1_1.txt", "r") as f:
        lines = f.readlines()

    numbers = [line.split("\n")[0] for line in lines]
    left = [int(number.split("  ")[0]) for number in numbers]
    right = np.array([int(number.split("  ")[1]) for number in numbers])
    total_score = 0
    for number in left:
        score = len(right[right == number])
        total_score += score * number

    print(total_score)