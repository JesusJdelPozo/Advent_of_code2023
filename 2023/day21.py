import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt

NEIGHBOURS = np.array([[-1, 0],  [1, 0], [0, -1], [0, 1]])
MOVES = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
def read_pattern(lines):
    p = []
    for line in lines:
        p.append(np.array([char for char in line]))
    return np.array(p)


def get_pattern(file):
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip("\n") for line in lines]

    pattern = read_pattern(lines)
    return pattern.reshape((len(pattern[0]), len(pattern[0])))


def step(pos, pattern):
    next_steps = []
    for neig in NEIGHBOURS:
        trial_row, trial_col = neig + pos
        if 0 <= trial_row < pattern.shape[0] and 0 <= trial_col < pattern.shape[1]:
            if pattern[trial_row, trial_col] == ".":
                next_steps.append([trial_row, trial_col])
    return next_steps

def step_inf(pos, pattern):
    next_steps = []
    row, col, row_p, col_p = pos
    pos = row + row_p * pattern.shape[0], col + col_p * pattern.shape[0]
    for neig in NEIGHBOURS:
        trial_row, trial_col = neig + pos
        if 0 <= trial_row < pattern.shape[0] and 0 <= trial_col < pattern.shape[1]:
            if pattern[trial_row, trial_col] == ".":
                next_steps.append([trial_row, trial_col])
    return next_steps

def plot_pattern(pattern):
    extended_pattern = np.zeros(pattern.shape, dtype=np.float64)
    for i in range(extended_pattern.shape[0]):
        for j in range(extended_pattern.shape[1]):
            if pattern[i, j] == ".":
                extended_pattern[i,j] = 0
            elif pattern[i, j] == "#":
                extended_pattern[i, j] = 1
            elif pattern[i, j] == "O":
                extended_pattern[i, j] = 2

    # extended_pattern = np.vstack([extended_pattern, extended_pattern, extended_pattern])
    # extended_pattern = np.hstack([extended_pattern, extended_pattern, extended_pattern])
    plt.imshow(extended_pattern)
    plt.show()
def expand_pattern(pattern):
    pattern = np.vstack([pattern, pattern, pattern])
    pattern = np.hstack([pattern, pattern, pattern])
    x, y = pattern.shape[0]//2, pattern.shape[1]//2
    return [[x, y]], pattern

def main():
    pattern = get_pattern("input day21.txt")
    pattern = pattern
    start = np.argwhere(pattern == "S")
    pounds = np.argwhere(pattern == "#")
    pattern[start[0][0], start[0][1]] = "."
    start, pattern = expand_pattern(pattern)


    n_steps = 131 + 65
    # cycles = n_steps//pattern.shape[1]
    # rest = n_steps % pattern.shape[1] + 1
    # left_rest = np.concatenate([pattern[5, pattern.shape[1]//2::-1], pattern[5, -1:pattern.shape[1]//2:-1]])
    # right_rest = np.concatenate([pattern[5, pattern.shape[1]//2:], pattern[5, :pattern.shape[1]//2]])
    # left_rest = left_rest[:rest]
    # right_rest = right_rest[:rest]
    # for i in range(2):
    #     if right_rest[rest-3] == "#" or right_rest[rest-4] == "#":
    #         right_rest[rest-i-1] = "#"
    #     if left_rest[rest-3] == "#" or left_rest[rest-4] == "#":
    #         left_rest[rest-i-1] = "#"
    # print(left_rest)
    # print(right_rest)
    # print(left_rest, right_rest, rest)
    # points = cycles * len(np.argwhere(pattern[5, :] == ".")) + len(np.argwhere(left_rest[:rest] == ".")) + len(np.argwhere(right_rest[:rest] == "."))
    # print(points)
    # print(pattern)+ len(np.argwhere(right_rest[:rest] = "."))
    # for p in pounds:
    #     pattern[p[0], p[1]] = "."
    # pattern[2,5] = "#"
    # pattern[pattern.shape[0]-1-2, 5] = "#"
    # pattern[5, 2] = "#"
    # pattern[5, pattern.shape[1]-3] = "#"
    # # print(pattern)
    pattern[start[0][0], start[0][1]] = "."
    t1 = perf_counter()
    even_field = pattern.copy()
    odd_field = pattern.copy()
    flag_even = True
    flag_odd = True
    for i in range(n_steps):
        new_positions = []
        field = pattern.copy()
        for pos in start:
            candidates = step(pos, pattern)
            for candidate in candidates:
                if candidate not in new_positions:
                    new_positions.append(candidate)
        #
        for pos in new_positions:
            field[pos[0], pos[1]] = "O"
        if i % 2 == 0:
            if np.all(np.equal(field, even_field)):
                print("EVEN", i)
                first_even = i
                flag_even = False
            if flag_even:
                even_field = field.copy()
        else:
            if np.all(np.equal(field, odd_field)):
                print("ODD", len(start))
                first_odd = len(start)
                break
            if flag_odd:
                odd_field = field.copy()

        start = new_positions
        if i == 64:
            print("Number of flips at 65 steps = ", len(start))
            plot_pattern(field)

    plot_pattern(field)
    print(len(start))
    print(perf_counter() - t1)



# 7218

if __name__ == '__main__':
    main()