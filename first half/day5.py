import numpy as np
from time import perf_counter


def day5_0(lines):
    def map_walk(init, idx):
        new_init = init
        i = map_indexes[idx] + 1
        while lines[i] != "":
            new_start, old_start, map_range = lines[i]
            if old_start <= init < old_start + map_range:
                new_init = new_start + init - old_start
                break
            i += 1

        if idx == len(map_indexes) - 2:
            return new_init
        else:
            idx = idx + 1
            return map_walk(new_init, idx)

    lines = [line.strip("\n") for line in lines]

    seeds = lines[0].split(":")[1].split(" ")

    map_indexes = [i for i, line in enumerate(lines) if "-to-" in line]
    map_indexes.append(len(lines) - 1)
    for j in range(len(map_indexes) - 1):
        for i in range(map_indexes[j] + 1, map_indexes[j + 1] - 1):
            lines[i] = [int(numb) for numb in lines[i].split(" ")]

    min_location = 1000000000000
    min_seed = 0
    for seed in seeds[1::2]:
        seed = int(seed)
        loc = map_walk(seed, 0)

        if loc < min_location:
            min_location = loc
            min_seed = seed

    print(min_location, min_seed)
    return min_location, min_seed


def day5_1(lines):
    lines = [line.strip("\n") for line in lines]
    seeds = lines[0].split(":")[1].split(" ")
    map_indexes = [i for i, line in enumerate(lines) if "-to-" in line]
    map_indexes.append(len(lines) - 1)
    for j in range(len(map_indexes) - 1):
        for i in range(map_indexes[j] + 1, map_indexes[j + 1] - 1):
            lines[i] = [int(numb) for numb in lines[i].split(" ")]

    def inverse_map_walk(init, idx, min_range):
        new_init = init
        i = map_indexes[idx] + 1
        # print(idx, map_indexes[idx], init)
        while lines[i] != "":
            new_start, old_start, map_range = lines[i]

            if new_start <= init < new_start + map_range:
                new_init = old_start + init - new_start
                step_range = old_start + map_range - new_init
                if step_range < min_range:
                    # print("new_range", step_range, min_range, new_start, map_range, new_init)
                    min_range = max([1, step_range])
                break
            i += 1

        if idx == 0:
            return new_init, min_range
        else:
            idx = idx - 1
            return inverse_map_walk(new_init, idx, min_range)
    i = 0
    flag = True
    while flag:
        min_range = 1000000000000000
        seed, min_range = inverse_map_walk(i, len(map_indexes) - 2, min_range)
        for j in range(1, len(seeds), 2):
            if int(seeds[j]) <= seed < int(seeds[j]) + int(seeds[j + 1]):
                print("result", i, seed)
                flag = False
                break
        # print("consumend", min_range)
        i += min_range
        if np.mod(i, 10000000) == 0:
            print(i)


def main():
    with open("input day5.txt") as f:
        lines = f.readlines()
    t1 = perf_counter()
    day5_1(lines)
    print(perf_counter() - t1)


if __name__ == '__main__':
    main()

