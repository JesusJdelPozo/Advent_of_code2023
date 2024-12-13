import numpy as np
from collections import defaultdict


def is_valid_update(update, rules):
    for i, page in enumerate(update):
        for j in range(i, len(update)):
            if page in rules[update[j]]:
                return False

    return True


if __name__ == '__main__':
    with open("input_day_5_1.txt", "r") as f:
        lines = f.readlines()

    lines = np.array([line.strip("\n") for line in lines])
    break_index = np.argwhere(lines == "").flatten()[0]
    rules = defaultdict(list)
    for line in lines[:break_index]:
        rules[line.split("|")[0]].append(line.split("|")[1])

    updates = [line.split(",") for line in lines[break_index + 1:]]
    total_sum = 0
    for update in updates:
        if is_valid_update(update, rules):
            total_sum += np.int_(update[len(update) // 2])

    print(total_sum)
