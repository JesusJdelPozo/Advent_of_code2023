import numpy as np
from day_6_1 import walk_path, turn

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
    obstacles_positions = np.argwhere(walked_matrix == "X")
    loops = 0
    matrix1 = matrix.copy()
    for position in obstacles_positions:
        i, j = position
        matrix = matrix1.copy()
        matrix[i, j] = "#"
        initial_position = np.argwhere(matrix1 == "^").flatten()
        delta = np.array([-1, 0])
        hare = 1
        turtle = 0
        while True:
            next_position = initial_position + delta
            if np.any(next_position < 0) or np.any(next_position >= matrix.shape[0]):
                    break

            if matrix[next_position[0], next_position[1]] == "#":
                delta = turn(delta)

            else:
                if matrix[initial_position[0], initial_position[1]] == ".":
                    matrix[initial_position[0], initial_position[1]] = "X"
                    hare += 1
                elif matrix[initial_position[0], initial_position[1]] == "X":
                    turtle += 1

                initial_position = next_position

            if turtle == hare:
                loops += 1
                break


    print(loops)
