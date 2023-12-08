import numpy as np


class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def walk(self, direction: str):
        if direction == 'L':
            return self.left
        elif direction == 'R':
            return self.right
        else:
            print("Not a valid direction")


def parse(tree, start, directions):
    p = 0
    while start != "":
        start = tree[start].walk(directions[p])
        yield start
        p = np.mod(p + 1, len(directions))


def day8_0(tree, directions):
    start = "AAA"
    end = "ZZZ"
    path = parse(tree, start, directions)
    result = 0
    while end != start:
        start = next(path)
        result += 1
    print(result)


def day8_1(tree, directions):
    starts = [key for key in tree.keys() if key[2] == "A"]
    paths = [parse(tree, start, directions) for start in starts]
    counts = []
    count = 0
    while len(counts) != 6:
        next_step = [next(path) for path in paths]
        count += 1
        for point in next_step:
            if point[2] == "Z":
                counts.append(count)

    result = np.lcm.reduce(np.int64(counts))
    print(result)


def main():
    with open("input day8.txt") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines]
    directions = lines[0]
    print(directions)
    tree_keys = [line.split("=")[0].strip(" ") for line in lines[1:] if line != ""]
    tree_lefts = [line.split("=")[1].split(",")[0].strip(" (") for line in lines[1:] if line != ""]
    tree_rights = [line.split("=")[1].strip(")").split(",")[1].strip(" ") for line in lines[1:] if line != ""]
    tree = {key: Node(key, left, right) for key, left, right in zip(tree_keys, tree_lefts, tree_rights)}
    day8_1(tree, directions)
    day8_0(tree, directions)


if __name__ == '__main__':
    main()