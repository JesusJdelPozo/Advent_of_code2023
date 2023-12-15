import numpy as np
from time import perf_counter


def read_pattern(lines):
    p = []
    for line in lines:
        p.append(np.array([char for char in line]))
    return np.array(p)


def tilt(direction, pattern):
    if direction == "N":
        reverse = True
        return operate_up_down(pattern, reverse)
    elif direction == "S":
        reverse = False
        return operate_up_down(pattern, reverse)
    elif direction == "W":
        reverse = True
        return operate_left_right(pattern, reverse)
    elif direction == "E":
        reverse = False
        return operate_left_right(pattern, reverse)
    return -1


def sort_line(line, reversed: bool):
    if reversed:
        return np.flip(np.sort(line))
    else:
        return np.sort(line)


def operate_up_down(pattern, reversed: bool):
    p_in_lines = [np.argwhere(pattern[:, i] == "#").flatten() for i in range(pattern.shape[0])]
    field = pattern.copy()
    for i in range(pattern.shape[0]):
        ini = 0
        for j in p_in_lines[i]:
            field[ini:j, i] = sort_line(pattern[ini:j, i], reversed)
            ini = j+1
        field[ini:, i] = sort_line(pattern[ini:, i], reversed)
    return field


def operate_left_right(pattern, reversed: bool):
    p_in_lines = [np.argwhere(pattern[i] == "#").flatten() for i in range(pattern.shape[0])]
    field = pattern.copy()
    for i in range(pattern.shape[0]):
        ini = 0
        for j in p_in_lines[i]:
            field[i, ini:j] = sort_line(pattern[i, ini:j], reversed)
            ini = j+1
        field[i, ini:] = sort_line(pattern[i, ini:], reversed)
    return field

def cycle(patern):
    north = tilt("N", patern)
    west = tilt("W", north)
    south = tilt("S", west)
    return tilt("E", south)

def get_pattern(file):
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip("\n") for line in lines]

    pattern = read_pattern(lines)
    return pattern.reshape((len(pattern[0]), len(pattern[0])))


def main():
    pattern = get_pattern("input day14.txt")
    t1 = perf_counter()
    field = pattern.copy()
    fields = []
    flag = False
    for i in range(100000):
        field = cycle(field)
        for f in fields:
            f, j = f
            if np.all(np.equal(f, field)):
                cycle_size = i-j
                offset = j
                flag = True
                print(i, j, i-j)
                break

        if flag:
            break
        fields.append([field, i])

    fields = [field for field, j in fields]
    offset_fields = fields[:offset]
    fields = fields[offset:]
    print(len(fields), len(offset_fields), offset)
    cycle_number = (1_000_000_000 - offset) % cycle_size
    field2 = fields[cycle_number-1]
    print(perf_counter() - t1)
    total = 0
    # print(4*(perf_counter() - t1))
    # print(field)
    for i in range(field2.shape[0]):
        for j in range(field2.shape[1]):
            if field2[j, i] == "O":
                total += (field2.shape[0] - j)
    print(total)


if __name__ == '__main__':
    main()

# too high 101361