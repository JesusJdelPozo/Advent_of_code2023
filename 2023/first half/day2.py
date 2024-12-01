import numpy as np
CUBES = {"red": 12, "green": 13, "blue": 14}


def day2_0(lines):
    valid_games = []
    for line in lines:
        idx = line.split(":")
        line_wo_header = idx[1]
        game_idx = int(idx[0][-2:])
        parts = line_wo_header.split(";")
        for part in parts:
            hands = part.split(",")
            valid = validate_hands(hands)
            if not valid:
                break
        if valid:
            if game_idx == 0:
                game_idx = 100
            valid_games.append(game_idx)
        print(game_idx, parts, valid)
        print(np.sum(np.array(valid_games)))
def validate_hands(hands):
    valid = True
    for hand in hands:
        groups = hand.split(",")
        # print(groups[0])
        if "red" in groups[0]:
            if int(groups[0][:3]) > CUBES["red"]:
                valid = False
                break

        if "green" in groups[0]:
            # print("green", groups[0][:3])
            if int(groups[0][:3]) > CUBES["green"]:
                valid = False
                break

        if "blue" in groups[0]:
            if int(groups[0][:3]) > CUBES["blue"]:
                valid = False
                break
    return valid


def day2_1(lines):
    hand_powers = []
    for line in lines:
        idx = line.split(":")
        line_wo_header = idx[1]
        game_idx = int(idx[0][-2:])
        parts = line_wo_header.split(";")
        hand_powers.append(find_powers(parts))
    print(np.sum(hand_powers))


def find_powers(parts):
    red = 0
    green = 0
    blue = 0
    for part in parts:
        hands = part.split(",")
        for hand in hands:
            groups = hand.split(",")
            # print(groups[0])
            if "red" in groups[0]:
                if int(groups[0][:3]) > red:
                    red = int(groups[0][:3])
            if "green" in groups[0]:
                if int(groups[0][:3]) > green:
                    green = int(groups[0][:3])
            if "blue" in groups[0]:
                if int(groups[0][:3]) > blue:
                    blue = int(groups[0][:3])
        print(hands, red, green, blue)
    return red * green * blue




def main():
    with open("input day2.txt") as f:
        lines = f.readlines()
    day2_1(lines)


if __name__ == '__main__':
    main()