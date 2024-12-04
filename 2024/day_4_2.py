import numpy as np


def is_x_mas(matrix, indices):
    x, y = indices
    pattern = "".join([matrix[x - 1, y - 1], matrix[x - 1, y + 1], matrix[x + 1, y + 1], matrix[x + 1, y - 1]])
    good_paterns = ["MSSM", "MMSS", "SSMM", "MSSM", "SMMS"]
    if matrix[x, y] == "A":
        if pattern in good_paterns:
            return True
        else:
            return False


if __name__ == '__main__':
    with open("input_day_4_1.txt", "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines if line != ""]
    matrix = np.zeros((len(lines), len(lines[0])), dtype=np.str_)
    for i, line in enumerate(lines):
        matrix[i, :] = [char for char in line]

    xmas_count = 0
    for i in range(1, matrix.shape[0] - 1):
        for j in range(1, matrix.shape[1] - 1):
            if is_x_mas(matrix, (i, j)):
                xmas_count += 1

    print(xmas_count)
