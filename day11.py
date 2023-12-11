import numpy as np


def main():
    with open("input day11.txt") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines if line != ""]
    matrix = np.zeros((len(lines), len(lines[0])), dtype=np.str_)
    for i, line in enumerate(lines):
        matrix[i, :] = [char for char in line]

    expansion_factor = 2  # 1000000 for part 2
    x_exp = [i for i in range(matrix.shape[0]) if "#" not in matrix[i, :]]
    y_exp = [j for j in range(matrix.shape[1]) if "#" not in matrix[:, j]]
    galaxies = [(i, j) for i in range(matrix.shape[0])
                for j in range(matrix.shape[1]) if matrix[i, j] == "#"]
    total = 0
    for g, galaxy in enumerate(galaxies):
        i, j = galaxy
        for gg in range(g+1, len(galaxies)):
            ii = min(i, galaxies[gg][0])
            iig = max(i, galaxies[gg][0])
            xcrosings = 0
            for xx in x_exp:
                if xx in range(ii, iig+1):
                    xcrosings += 1
            jj = min(j, galaxies[gg][1])
            jjg = max(j, galaxies[gg][1])
            ycrosings = 0
            for yy in y_exp:
                if yy in range(jj, jjg+1):
                    ycrosings += 1

            xdist = abs(i-galaxies[gg][0]) + xcrosings*expansion_factor - xcrosings
            ydist = abs(j - galaxies[gg][1]) + ycrosings*expansion_factor - ycrosings
            total += xdist + ydist

    print(total)


if __name__ == '__main__':
    main()