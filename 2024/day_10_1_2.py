import numpy as np


def in_limits(pos, upper):
    return not (np.any(pos < 0) or np.any(pos >= upper))


def get_nb_tail_head_1(position, matrix, result):
    deltas = np.array([(0, -1), (0, 1), (-1, 0), (1, 0)])
    candidates = position + deltas
    candidates = [candidate for candidate in candidates if in_limits(candidate, matrix.shape[0])]
    next_points = [pos for pos in candidates if int(matrix[*position]) + 1 == int(matrix[*pos])]
    for n in next_points:
        if matrix[*n] == "9":
            result.append(1)
            matrix[*n] = "0"
        elif matrix[*n] == "0":
            pass
        else:
            get_nb_tail_head_1(n, matrix, result)


def get_nb_tail_head_2(position, matrix, result):
    deltas = np.array([(0, -1), (0, 1), (-1, 0), (1, 0)])
    candidates = position + deltas
    candidates = [candidate for candidate in candidates if in_limits(candidate, matrix.shape[0])]
    next_points = [pos for pos in candidates if int(matrix[*position]) + 1 == int(matrix[*pos])]
    for n in next_points:
        if matrix[*n] == "9":
            result.append(1)
        else:
            get_nb_tail_head_2(n, matrix, result)


if __name__ == '__main__':
    with open("input_day_10_1.txt", "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines if line != ""]
    matrix = np.zeros((len(lines), len(lines[0])), dtype=np.str_)
    for i, line in enumerate(lines):
        matrix[i, :] = [char for char in line]

    print(matrix)
    total = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix[1])):
            result = []
            if matrix[i, j] == "0":
                test_matrix = matrix.copy()
                get_nb_tail_head_1((i, j), test_matrix, result)
                # print("Head at row =", i, "col =", j, "had a result =", len(result))
                total += len(result)

    print("First part result: ", total)

    total = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix[1])):
            result = []
            if matrix[i, j] == "0":
                test_matrix = matrix.copy()
                get_nb_tail_head_2((i, j), test_matrix, result)
                # print("Head at row =", i, "col =", j, "had a result =", len(result))
                total += len(result)

    print("Second part result: ", total)



