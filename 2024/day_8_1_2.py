import numpy as np


def draw_nodes_1(positions, limits, final):
    nb_nodes = 0
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i != j:
                delta = positions[i] - positions[j]
                trial = positions[i] + delta
                if 0 <= trial[0] < limits[0] and 0 <= trial[1] < limits[1]:
                    final[trial[0], trial[1]] = "#"


def draw_nodes_2(positions, limits, final):
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i != j:
                delta = positions[i] - positions[j]
                for k in range(50):
                    trial = positions[i] + k * delta
                    if 0 <= trial[0] < limits[0] and 0 <= trial[1] < limits[1]:
                        final[trial[0], trial[1]] = "#"
                    else:
                        break


if __name__ == '__main__':
    with open("input_day_8_1.txt", "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines if line != ""]
    matrix = np.zeros((len(lines), len(lines[0])), dtype=np.str_)
    for i, line in enumerate(lines):
        matrix[i, :] = [char for char in line]

    simbols = list({s for s in matrix.flatten() if s != "."})
    final_matrix = matrix.copy()
    for simbol in simbols:
        positions = np.argwhere(matrix == simbol)
        draw_nodes_1(positions, matrix.shape, final_matrix)

    print("First part :", len(final_matrix[final_matrix == "#"]))
    final_matrix = matrix.copy()
    for simbol in simbols:
        positions = np.argwhere(matrix == simbol)
        draw_nodes_2(positions, matrix.shape, final_matrix)

    print("Second part :", len(final_matrix[final_matrix == "#"]))
