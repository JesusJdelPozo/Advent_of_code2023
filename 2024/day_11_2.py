import numpy as np
from time import perf_counter


def stone_spliter(stone, iterations_left):
    rest = []
    if stone == "0":
        stone = "1"

    elif np.mod(len(stone), 2) == 0 and len(stone) > 1:
        rest = [{str(int(stone[len(stone) // 2:])): iterations_left}]
        stone = str(int(stone[:len(stone) // 2]))

    else:
        stone = str(int(stone) * 2024)

    return stone, rest


def update_history(key, history, next_stone, new_rest):
    iteration = history[stone]["last_iteration"]
    result = history[stone][iteration]["result"]
    rest = history[stone][iteration]["rest"]
    result += len(new_rest)
    next_rest = rest + new_rest
    history[stone]["last_iteration"] = iteration + 1
    history[stone][iteration + 1] = {"result": result, "next_stone": next_stone, "rest": next_rest}
    return history


def learn_from_hitory(total_rest, history):
    new_total_rest = []
    new_stones = []
    score = 0
    for candidate in total_rest:
        for key, value in candidate.items():
            if key in history.keys():
                if value in history[key].keys():
                    score += history[key][value]["result"]
                    new_stones.append(key)
            else:
                new_total_rest.append(candidate)

    return new_total_rest, score, new_stones


if __name__ == '__main__':
    with open("input_day_11_1.txt", "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines if line != ""]
    stones = lines[0].split(" ")
    # stones = ["125", "17"]
    total = 0
    # for stone in stones:
    # t1 = perf_counter()
    stones = ["17"]
    # stones = ["0"]

    t1 = perf_counter()
    total_result = 0
    history = {}
    stone_final = []
    for stone in stones:
        nb_iter = 7
        iteration = 0
        total_rest = []
        for i in range(100000):
            if stone not in history.keys():
                history[stone] = {"last_iteration": 0, 0: {"result": 1, "next_stone": None, "rest": []}}
            new_stone = stone

            for j in range(nb_iter):
                new_stone, new_rest = stone_spliter(new_stone, nb_iter - j - 1)
                history = update_history(stone, history, new_stone, new_rest)

            stone_final.append(new_stone)
            # print(total_rest, history[stone][history[stone]["last_iteration"]]["rest"] )
            total_rest = history[stone][history[stone]["last_iteration"]]["rest"] + total_rest
            total_result += len(history[stone][history[stone]["last_iteration"]]["rest"])
            print([(key, value) for key, value in history.items()])
            # print("Last iteration", total_rest)
            if np.mod(i, 100000) == 0:
                print(i, len(total_rest))

            total_rest, score, new_stones = learn_from_hitory(total_rest, history)
            # print(new_stones, stone_final)
            for s in new_stones:
                stone_final.append(s)

            total_result += score
            # print(history)
            print("score and result", score, total_result)
            print(new_stones, stone_final)
            if len(total_rest) == 0:
                print("Result: ", i)
                break
            if len(total_rest) > 0:
                next = total_rest.pop(0)
                for k, v in next.items():
                    stone = k
                    nb_iter = v

    print(perf_counter() - t1)
    # ['2097446912', '14168', '4048', '2', '0', '2', '4', '40', '0', '48', '2', '8', '6', '7', '6', '0', '3', '2']
    print("Final Result: ", total_result, stone_final)
