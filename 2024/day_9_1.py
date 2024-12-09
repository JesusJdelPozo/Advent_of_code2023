

if __name__ == '__main__':
    with open("input_day_9_1.txt", "r") as f:
        lines = f.readlines()

    test = ["2333133121414131402"]
    lines = test
    lines = [c for c in lines[0]]

    values = lines[:: 2]
    spaces = lines[1:: 2]
    print(values)
    print(spaces)
    if len(values) > len(spaces):
        spaces.append("0")
    id = 0
    message = []
    for value, space in zip(values, spaces):
        message += [id] * int(value) + ["."] * int(space)
        id += 1

    print(message)
    forward = 0
    for i in range(len(message)):
        backward = len(message) - 1
        while message[backward] == ".":
            backward -= 1
        if backward <= i:
            break
        if message[i] == ".":
            message[i], message[backward] = message[backward], message[i]


    total = 0
    for i in range(len(message)):
        if message[i] == ".":
            break
        total += i * int(message[i])

    print(total)
