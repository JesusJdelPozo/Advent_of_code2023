class PlutoStone:
    def __init__(self, value):
        self.value = int(value)
        self.str_length = len(str(self.value))

    def blink(self):
        if self.value == 0:
            return PlutoStone(1), None
        elif self.str_length > 1 and self.str_length % 2 == 0:
            left = int(str(self.value)[:self.str_length // 2])
            right = int(str(self.value)[self.str_length // 2:])
            return PlutoStone(left), PlutoStone(right)
        else:
            return PlutoStone(self.value * 2024), None


def get_iterations(stone: PlutoStone, nb_iterations):
    it = nb_iterations - 1
    left, right = stone.blink()
    if it != 0:
        left_result = get_iterations(left, it)
        right_result = 0
        if right is not None:
            right_result = get_iterations(right, it)

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
    for value in stone_values:
        stone = PlutoStone(value)
        result = get_iterations(stone, 25)
        total += result

    print(total)
