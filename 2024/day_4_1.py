import numpy as np


def get_neighbors(matrix, indices):
    neighbors = []
    for dx, dy in [(0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)]:
        x, y = indices
        nx, ny = x + dx, y + dy
        if 0 <= nx < matrix.shape[0] and 0 <= ny < matrix.shape[1]:
            neighbors.append((matrix[nx, ny], (dx, dy)))

    return neighbors


if __name__ == '__main__':
    with open("input_day_4_1.txt", "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines if line != ""]
    matrix = np.zeros((len(lines), len(lines[0])), dtype=np.str_)
    for i, line in enumerate(lines):
        matrix[i, :] = [char for char in line]

    xmas_count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] == "X":
                neighbors = get_neighbors(matrix, (i, j))
                for neighbor in neighbors:
                    if neighbor[0] == "M":
                        dx, dy = neighbor[1]
                        if 0 <= i + 3*dx < matrix.shape[0] and 0 <= j + 3*dy < matrix.shape[1]:
                            if matrix[i + 2*dx, j + 2*dy] == "A" and matrix[i + 3*dx, j + 3*dy] == "S":
                                xmas_count += 1

    print(xmas_count)


