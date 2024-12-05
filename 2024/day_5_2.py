import numpy as np
from collections import defaultdict
from day_5_1 import is_valid_update


def reorder_update(update, rules):
    ordered = update.copy()
    for i, page in enumerate(update):
        for j in range(i, len(update)):
            if page in rules[update[j]]:
                ordered[j], ordered[i] = ordered[i], ordered[j]
    if is_valid_update(ordered, rules):
        return ordered
    else:
        update = ordered.copy()
        return reorder_update(update, rules)


if __name__ == '__main__':
    with open("input_day_5_1.txt", "r") as f:
        lines = f.readlines()

    lines = np.array([line.strip("\n") for line in lines])
    break_index = np.argwhere(lines == "").flatten()[0]
    rules = defaultdict(list)
    for line in lines[:break_index]:
        rules[line.split("|")[0]].append(line.split("|")[1])

    updates = [line.split(",") for line in lines[break_index + 1:]]
    total_invalid_sum = 0
    for update in updates:
        if not is_valid_update(update, rules):
            ordered_update = reorder_update(update, rules)
            total_invalid_sum += np.int_(ordered_update[len(update) // 2])

    print(total_invalid_sum)
