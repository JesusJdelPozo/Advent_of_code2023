import numpy as np

def hash_lens(label):
    hash_value = 0
    for char in label:
        hash_value += ord(char)
        hash_value *= 17
        hash_value = np.mod(hash_value, 256)
    return int(hash_value)


def main():
    with open("input day15.txt") as f:
        lines = f.readlines()
    keys = lines[0].split(",")
    print("part 1 =", sum([hash_lens(key) for key in keys]))
    boxes = {}
    for i, key in enumerate(keys):
        label = "". join([char for char in key if char not in ["=", "-","1", "2", "3", "4", "5", "6", "7", "8", "9"]])
        action = "".join([char for char in key if char in ["=", "-"]])
        focal = "".join([char for char in key if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]])
        if action == "=":
            box = hash_lens(label)
            dbox = boxes.get(box, {})
            dbox[label] = focal
            boxes[box] = dbox
        elif action == "-":
            k = hash_lens(label)
            if k in boxes.keys():
                box = boxes[k]
                if label in box.keys():
                    box.pop(label)
    total = 0
    for i in range(256):
        if i in boxes.keys():
            box = boxes[i]
            for j, key in enumerate(box.keys()):
                focal_power = (i+1) * (j+1) * int(box[key])
                total += focal_power
    print("part 2 =", total)


if __name__ == '__main__':
    main()