import numpy as np

NEIGHBORS = {"R":[0, 1], "L": [0, -1], "D":[1, 0], "U": [-1, 0]}
pipes = {"|": ["U", "D"],
         "-": ["L", "R"],
         "L": ["U", "R"],
         "J": ["L", "U"],
         "7": ["L", "D"],
         "F": ["R", "D"]}
inverse = {"U": "D", "D": "U", "L": "R", "R": "L"}
SIZE = 140
SIZE1 = 140
SIZE2 = 140

def update_position(position, direction):
    i = position[0] + NEIGHBORS[direction][0]
    j = position[1] + NEIGHBORS[direction][1]
    return [i, j]

def get_pipe(position, direction, matrix):
    i = position[0] + NEIGHBORS[direction][0]
    j = position[1] + NEIGHBORS[direction][1]
    if matrix[i, j] in pipes.keys():
        return matrix[i, j]
    else:
        return ""
def main():
    with open("input day10.txt") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines if line != ""]
    matrix = np.zeros((len(lines), len(lines[0])), dtype=np.str_)
    for i, line in enumerate(lines):
        matrix[i, :] = [char for char in line]

    ## day10_0
    start = np.argwhere(matrix == "S")[0]
    possible_moves = {}
    for key, values in pipes.items():
        for value in values:
            new_pipe = get_pipe(start, value, matrix)
            if new_pipe:
                if inverse[value] in pipes[new_pipe]:
                    l = possible_moves.get(key, [])
                    l.append(value)
                    possible_moves[key] = l

    possible_initial_pipe = {key: value for key, value in possible_moves.items() if len(value) == 2}
    initial_keys = [key for key in possible_initial_pipe.keys()]
    matrix[start[0], start[1]] = initial_keys[0]
    move = possible_initial_pipe[initial_keys[0]][0]
    pos = start.copy()
    path =[]
    for i in range(SIZE * SIZE):
        next_pipe = get_pipe(pos, move, matrix)
        path.append(list(pos))
        pos = update_position(pos, move)
        for value in pipes[next_pipe]:
            if value != inverse[move]:
                new_move = value
        move = new_move
        next_pos = pos
        if next_pos[0] == start[0] and next_pos[1] == start[1]:
            break

    print("day10_0=", len(path)//2)

    # day10_1
    x, y = matrix.shape
    for k, pos in enumerate(path):
        i, j = pos
        ik, jk = path[k + 1]
        if jk > j:
            break

    matrix2 = np.zeros((x+2, y+2))
    for i in range(len(path)):
        ii = np.mod((k + i), len(path))
        kk = np.mod((k + i + 1), len(path))
        i, j = path[ii]
        ik, jk = path[kk]
        if jk > j:
            factor = 2
        elif jk < j:
            factor = 1
        matrix2[1+i, 1+j] = factor

    count = 0
    for j in range(matrix2.shape[1]):
        flag = False
        ones = [numb for numb in matrix2[:, j] if numb > 0]
        if ones:
            updown = ones[0]

        ones = len(ones)
        for i in range(matrix2.shape[0]):
            if matrix2[i, j] > 0:
                ones -= 1
                if updown == matrix2[i, j]:
                    flag = not flag
                    if int(updown) == 1:
                        updown = 2
                    else:
                        updown = 1
            if flag and matrix2[i, j] == 0 and ones > 0:
                count += 1

    print(count)

if __name__ == '__main__':
    main()