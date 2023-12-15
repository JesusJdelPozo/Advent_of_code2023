import numpy as np


def fprev(number):
    return patern(number, 0)


def fnext(number):
    return patern(number, -1)


def patern(arr, idx):
    if np.all(arr == 0):
        return arr[idx]
    else:
        return arr[idx] + ((-1) ** abs(idx+1)) * patern(arr[1:] - arr[:-1], idx)


def main():
    with open("input day9.txt") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines if line != ""]
    numbers = [np.int64(line.split(" ")) for line in lines]
    next_numbers = [fnext(number) for number in numbers]
    print(np.sum(next_numbers))
    prev_numbers = [fprev(number) for number in numbers]
    print(np.sum(prev_numbers))


if __name__ == '__main__':
    main()