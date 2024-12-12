import numpy as np
import queue

NEIGHBORS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
MOVES = {"u": (0, -1), "d": (0, 1), "l": (-1, 0), "r": (1, 0)}
IDX = {"u": 0, "d": 1, "l": 2, "r": 3}
DIRECTIONS = {"u": ["u", "l", "r"],
              "d": ["d", "l", "r"],
              "l": ["u", "d", "l"],
              "r": ["u", "d", "r"]}


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


def possible_jumps(pos, pattern):
    jumps = []
    direction = pos[2]
    for v in DIRECTIONS[direction]:
        i, j = MOVES[v]
        trial = (pos[0] + i, pos[1] + j)
        if 0 <= trial[0] < pattern.shape[0] and 0 <= trial[1] < pattern.shape[1]:
            jumps.append((trial[0], trial[1], v))
    return jumps


def reconstruct_path(previous, current, matrix):
    total_path = [current]
    g = matrix[current[0], current[1]]
    while current in previous.keys():
        current = previous[current]
        if not (current[0] == 0 and current[1] == 0):
            g += matrix[current[0], current[1]]
        total_path.append(current)
    return total_path[-1::-1], g


def is_valid(previous, new, current):
    v1 = current[2]
    prev1 = previous.get(current, (0, 0, "."))
    v2 = prev1[2]
    prev2 = previous.get(prev1, (0, 0, "."))
    v3 = prev2[2]
    if prev2[0] == 0 and prev2[1] == 0:
        v3 = "."
    if v1 == v2 and v2 == v3 and v3 == new[2]:
        print(v1, v2, v3, new[2])
        return False
    else:
        return True


def main():
    pattern = get_pattern("test input.txt")
    pattern = np.int64(pattern.transpose())
    start = (0, 0, "d")
    end = (pattern.shape[0] - 1, pattern.shape[1] - 1, "r")
    tiles = queue.PriorityQueue()
    tiles.put((0, start))
    gscores = np.full((pattern.shape[0], pattern.shape[1]), np.inf)
    gscores[0, 0] = 0
    fscore = np.full(pattern.shape, np.inf)
    fscore[0, 0] = 0
    previous = {}
    while tiles.qsize() > 0:
        tile = tiles.get()
        tile = tile[1]
        print(tile)
        if tile[0] == end[0] and tile[1] == end[1]:
            path = reconstruct_path(previous, tile, pattern)
            field = np.full(pattern.shape, 0)
            total = 0
            for step in path[0]:
                if not (step[0] == 0 and step[1] == 0):
                    total += pattern[step[0], step[1]]
                field[step[0], step[1]] = total

            print(total, "    total\n", field.transpose(), gscores[pattern.shape[0] - 1, pattern.shape[1] - 1])
            print("result", reconstruct_path(previous, tile, pattern))
            # break
        # path = reconstruct_path(previous, tile, pattern)
        # field = np.full(pattern.shape, ".")
        # for step in path[0]:
        #     field[step[0], step[1]] = "#"
        # print(field.transpose())
        # total += pattern[tile[0], tile[1]]
        new_tiles = possible_jumps(tile, pattern)
        print("1", new_tiles)
        for new in new_tiles:
            if is_valid(previous, new, tile):
                print("2", new_tiles)
                score = gscores[tile[0], tile[1]] + pattern[new[0], new[1]]
                if score < gscores[new[0], new[1]]:
                    print("3", new_tiles)
                    previous[new] = tile
                    gscores[new[0], new[1]] = score
                    f = score  # + abs(new[0] - end[0]) + abs(new[1] - end[1])
                    new_entry = (f, new)
                    tiles.put(new_entry)


if __name__ == '__main__':
    main()
