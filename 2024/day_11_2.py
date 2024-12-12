from day_11_1 import PlutoStone


def get_iterations(stone: PlutoStone, nb_iterations, history):
    it = nb_iterations - 1
    left, right = stone.blink()
    if it != 0:
        temp = {}
        if it in history.keys():
            temp = history[it]

        if left.value in temp.keys():
            left_result = temp[left.value]
        else:
            left_result = get_iterations(left, it, history)
            temp[left.value] = left_result

        history[it] = temp
        right_result = 0
        if right is not None:
            if right.value in temp.keys():
                right_result = temp[right.value]
            else:
                right_result = get_iterations(right, it, history)
                temp[right.value] = right_result

        history[it] = temp
        return left_result + right_result

    else:
        if right is not None:
            return 2
        else:
            return 1


if __name__ == '__main__':
    with open("input_day_11_1.txt", "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines if line != ""]
    stone_values = lines[0].split(" ")
    total = 0
    history = {}
    for value in stone_values:
        stone = PlutoStone(value)
        result = get_iterations(stone, 25, history)
        total += result

    print(total)
