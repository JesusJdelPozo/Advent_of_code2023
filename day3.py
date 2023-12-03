import numpy as np

NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# NOT_SYMBOLS = NUMBERS.append(".")
NEIGHBORS = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
SYMBOLS = ['@', '&', '+', '-', '/', '*', '$', '#', '=', '%']


def day3_0(lines):
    i = 0
    lines = [line.split("\n")[0] for line in lines]
    matrix = np.zeros((len(lines[0]), len(lines)), dtype=np.str_)
    x_len, y_len = matrix.shape
    numbers = []
    for j, line in enumerate(lines):
        matrix[:, j] = [line[i] for i in range(x_len)]
        numb = ""
        for i, k in enumerate(line):
            if (k == "." or k in SYMBOLS) and numb != "":
                numbers.append((numb, i - 1, j))
                numb = ""
            if k in NUMBERS:
                numb += k
        if numb != "":
            numbers.append((numb, i, j))

    parts = []
    part_numbers = []
    for number in numbers:
        if valid(number, matrix):
            parts.append(int(number[0]))
            part_numbers.append(number)
    print(np.sum(parts))
    return part_numbers, matrix


def valid(number, matrix):
    xini = number[1] - len(number[0]) + 1
    x_len, y_len = matrix.shape
    validation = False
    # print(xini, len(number[0]),number[1],matrix[xini : number[1]+1, number[2]])
    for i in range(xini, number[1] + 1):
        for ii, jj in NEIGHBORS:
            xidx = i + ii
            yidx = number[2] + jj
            if 0 <= xidx < x_len and 0 <= yidx < y_len:
                if matrix[xidx, yidx] in SYMBOLS:
                    validation = True

    return validation


def day3_1(valid_parts, matrix):
    stars = np.argwhere(matrix == "*")
    gear_ratios = []
    for star in stars:
        gear = []
        for part in valid_parts:
            xidx = part[1]
            yidx = part[2]
            px, py = star
            if py == yidx and (px-2 < xidx < px + 4):
                if matrix[px-1, yidx] in NUMBERS or matrix[px+1, yidx] in NUMBERS:
                    gear.append(part[0])
            if abs(yidx - py) == 1 and (px-2 < xidx < px + 4):
                if matrix[px-1, yidx] in NUMBERS or matrix[px+1, yidx] in NUMBERS or matrix[px, yidx] in NUMBERS:
                    gear.append(part[0])
        if len(gear) == 2:
            gear_ratios.append(int(gear[0])*int(gear[1]))
    print(sum(gear_ratios))

def main():
    with open("input day3.txt") as f:
        lines = f.readlines()
    valid_parts, matrix = day3_0(lines)
    day3_1(valid_parts, matrix)


if __name__ == '__main__':
    main()
