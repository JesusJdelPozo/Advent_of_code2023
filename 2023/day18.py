import numpy as np
import matplotlib.pyplot as plt
import sys



MOVES = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}


def main():
    with open("test input.txt") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines if line != ""]
    directions = [line.split(" ")[0] for line in lines]
    steps = [np.int_(line.split(" ")[1]) for line in lines]
    colors = [line.split(" ")[2].strip("()".upper()) for line in lines]
    colors = [(int(color[1:6], 16), int(color[6:], 16)) for color in colors]
    steps2 = [color[0] for color in colors]
    start = [0, 0]
    minx =10000
    maxx = 0
    miny = 10000
    maxy = 0
    rows = {}
    for direction, step in zip(directions, steps):
        start[0], start[1] = start[0] + step * MOVES[direction][0], start[1] + step * MOVES[direction][1]
        if start[0] < minx: minx = start[0]
        if start[0] > maxx: maxx = start[0]
        if start[1] < miny: miny = start[1]
        if start[1] > maxy: maxy = start[1]

    print(minx, maxx, miny, maxy)

    xrange = maxx - minx + 1
    yrange = maxy - miny + 1
    start = [-minx, -miny]
    print(xrange, yrange, start)
    factor = "D"
    for direction, step in zip(directions, steps):
        if direction == "U":
            # if factor == "D":
                # field[start[0], start[1]] = 1
            factor = "U"
        if direction == "D":
            # if factor == 1:
                # field[start[0], start[1]] = 2
            factor = "D"

        if start[1] in rows.keys():
            internal_list = rows[start[1]]
        else:
            internal_list = []
        s = start[0]
        d = step * MOVES[direction][0]
        if d == 0:
            d = 1
        internal_list.append((s, s + d, factor))
        rows[start[1]] = internal_list
        start[0], start[1] = start[0] + step * MOVES[direction][0], start[1] + step * MOVES[direction][1]

    sorted_keys = sorted(rows.keys())
    [print(key, rows[key]) for key in sorted_keys]
    scan = np.zeros(xrange)
    area = 0
    field2 = np.full((xrange, yrange), 0)
    for i, key in enumerate(sorted_keys):
        for value in rows[key]:
            if value[0] < value[1]:
                scan[value[0]:value[1]] = 1
        area += len(scan[scan == 1])
        field2[:, i] = scan
        for j, value in enumerate(rows[key]):
            if value[0] > value[1]:
                if value[2] == "U":
                    scan[value[1]:value[0]] = 0
                elif value[2] == "D":
                    scan[value[0]:value[1]: -1] = 0
                    if j + 1 < len(rows[key]):
                        if rows[key][j+1][2] == "U":
                            print("VALUES", j, value[0], value[1])
                            print("NEXT_VALUE", j+1, rows[key][j+1][0], rows[key][j+1][1] )
                            scan[rows[key][j+1][0]:rows[key][j+1][1]] = 0

        # print(scan)

        if i + 1 < len(sorted_keys):
            for kk in range(i+1, sorted_keys[i+1]):
                field2[:, kk] = scan
            area += (sorted_keys[i + 1] - sorted_keys[i] - 1) * len(scan[scan == 1])

    print(area)
    plt.imshow(field2.transpose())
    plt.show()
    field = np.full((xrange, yrange), 0)
    factor = 2
    i = 0
    for direction, step, color in zip(directions, steps, colors):
        for i in range(step):
            if direction == "U":
                if factor == 2:
                    field[start[0], start[1]] = 1
                factor = 1
            if direction == "D":
                if factor == 1:
                    field[start[0], start[1]] = 2
                factor = 2
            field[start[0] + MOVES[direction][0], start[1] + MOVES[direction][1]] = factor
            start[0], start[1] = start[0] + MOVES[direction][0], start[1] + MOVES[direction][1]
        i +=1


    count = 0
    for j in range(field.shape[1]):
        flag = False
        ones = [numb for numb in field[:, j] if numb > 0]
        if ones:
            updown = ones[0]

        ones = len(ones)
        for i in range(field.shape[0]):
            if field[i, j] > 0:
                ones -= 1
                if updown == field[i, j]:
                    flag = not flag
                    if int(updown) == 1:
                        updown = 2
                    else:
                        updown = 1
            if flag and field[i, j] == 0 and ones > 0:
                field[i, j] =3
                count += 1



    data = field
    plt.imshow(data.transpose())
    plt.show()
    # print(len(data[data>0]))



if __name__ == '__main__':
    main()


# 92440 92441 too low