import numpy
import numpy as np


def read_patterns(lines):
    patterns = []
    p = []
    for line in lines:
        if line == "":
            patterns.append(np.array(p))
            p = []
        else:
            p.append(np.array([char for char in line]))
    return patterns


def get_mirror(pattern):
    size = pattern.shape[0] - 1
    for i in range(size):
        r_mirror = min(i + 1 + i+1, size + 1)
        l_mirror = i - min(i, r_mirror-(i+2))
        check = np.argwhere(numpy.equal(pattern[l_mirror:i + 1, :], np.flip(pattern[i + 1:r_mirror, :], axis=0)) == False).flatten()
        if len(check) ==2:
            return i + 1
    return 0

def main():
    with open("input day13.txt") as f:
        lines = f.readlines()
    lines = [line.strip("\n") for line in lines]
    patterns = read_patterns(lines)
    patterns = [p.reshape((len(p), len(p[0]))) for p in patterns]
    h_lines = []
    v_lines = []
    for pattern in patterns:
        horizontal = get_mirror(pattern)
        p = pattern.copy()
        vertical = get_mirror(np.transpose(p))
        h_lines.append(np.int64(horizontal))
        v_lines.append(np.int64(vertical))

    total = [v + 100 * h for v, h in zip(v_lines, h_lines)]
    print(np.sum(total), total)


if __name__ == '__main__':
    main()
