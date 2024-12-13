import numpy as np


def turn(delta):
    if np.all(delta == [-1, 0]):
        return np.array([0, 1])
    elif np.all(delta == [0, 1]):
        return np.array([1, 0])
    elif np.all(delta == [1, 0]):
        return np.array([0, -1])
    elif np.all(delta == [0, -1]):
        return np.array([-1, 0])


def walk_path(initial, delta, input_matrix):
    matrix = input_matrix.copy()
    while True:
        next_position = initial + delta
        if np.any(next_position < 0) or np.any(next_position >= matrix.shape[0]):
            matrix[initial[0], initial[1]] = "X"
            break

        if matrix[next_position[0], next_position[1]] == "#":
            delta = turn(delta)

        else:
            if matrix[initial[0], initial[1]] != "X":
                matrix[initial[0], initial[1]] = "X"

            initial = next_position

    return matrix


if __name__ == '__main__':
    with open("input_day_6_1.txt", "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines if line != ""]
    matrix = np.zeros((len(lines), len(lines[0])), dtype=np.str_)
    for i, line in enumerate(lines):
        matrix[i, :] = [char for char in line]

    initial_position = np.argwhere(matrix == "^").flatten()
    delta = np.array([-1, 0])
    walked_matrix = walk_path(initial_position, delta, matrix)
    print(len(np.argwhere(walked_matrix == "X").flatten())//2)

