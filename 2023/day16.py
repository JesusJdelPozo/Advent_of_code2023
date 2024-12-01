import numpy as np
from collections import defaultdict
from time import perf_counter


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

def propagate(pos, matrix):
    i, j, direction = pos
    io, jo = i, j
    if direction == "r":
        if i + 1 < matrix.shape[0]:
            i += 1
    elif direction == "u":
        if j - 1 >= 0:
            j -= 1
    elif direction == "d":
        if j + 1 < matrix.shape[1]:
            j += 1
    elif direction == "l":
        if i - 1 >= 0:
            i -= 1
    if i != io or j != jo:
        new_directions = apply_operation(direction, matrix[i, j])
        new_position = [(i, j, d) for d in new_directions]
        return new_position
    return None

def apply_operation(direction, operation):
    match operation:
        case "|":
            if direction in ["l", "r"]:
                return ["u", "d"]
            else:
                return [direction]
        case "-":
            if direction in ["u", "d"]:
                return ["l", "r"]
            else:
                return [direction]
        case ".":
            return [direction]
        case "\\":
            match direction:
                case "u":
                    return ["l"]
                case "d":
                    return ["r"]
                case "r":
                    return ["d"]
                case "l":
                    return ["u"]
        case "/":
            match direction:
                case "u":
                    return ["r"]
                case "d":
                    return ["l"]
                case "r":
                    return ["u"]
                case "l":
                    return ["d"]

def day16_part_1(pos, pattern):
    old_pos = []
    tiles = [pos]
    field = np.full(pattern.shape, ".")
    while tiles:
        tile = tiles.pop(0)
        old_pos.append(tile)
        if 0 <= tile[0] < field.shape[0] and  0 <= tile[1] < field.shape[1]:
            field[tile[0], tile[1]] = "#"
        new_tiles = propagate(tile, pattern)
        if new_tiles:
            for tile in new_tiles:
                if tile not in old_pos:
                    tiles.append(tile)

    return np.size(field[field == "#"])


def main():
    pattern = get_pattern("input day16.txt")
    pattern = pattern.transpose()
    pos = (-1, 0, "r")
    print("part one", day16_part_1(pos, pattern))
    positions_l = [(-1, i, "r") for i in range(pattern.shape[0])]
    positions_r = [(pattern.shape[0], i, "l") for i in range(pattern.shape[0])]
    positions_u = [(i, -1, "d") for i in range(pattern.shape[1])]
    positions_d = [(i, pattern.shape[1], "u") for i in range(pattern.shape[1])]
    positions = positions_r + positions_l + positions_u + positions_d
    max_e = 0
    for pos in positions:
        e = day16_part_1(pos, pattern)
        if e > max_e:
            max_e = e
    print("part two", max_e)



if __name__ == '__main__':
    main()