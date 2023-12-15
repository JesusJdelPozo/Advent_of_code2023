import numpy as np

CARDS_NAME = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")


def modify_hand(hand: str):
    new_hand = []
    for c in hand:
        if c == "K":
            c = "Q"
        elif c == "Q":
            c = "K"
        elif c == "T":
            c = "A"
        elif c == "A":
            c = "T"
        elif c == "J":
            c = "1"
        new_hand.append(c)
    return "".join(new_hand)


def get_score(points):
    point = [value for value in points.values() if value > 0]
    point.sort()
    jokers = points["J"]
    if jokers > 0:
        p = []
        flag = False
        for i, j in enumerate(point):
            if j != jokers or flag:
                p.append(j)
            else:
                flag = True

        if jokers != 5:
            p[-1] += jokers
        else:
            p.append(jokers)
        print(jokers, point, p)
    else:
        p = point

    if len(p) == 1:
        return 7
    elif len(p) == 2:
        if 4 in p:
            return 6
        else:
            return 5
    elif len(p) == 3:
        if 3 in p:
            return 4
        else:
            return 3
    elif len(p) == 4:
        return 2
    else:
        return 1


def main():
    with open("input day7.txt") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines]
    hands = [line.split(" ")[0] for line in lines if line != ""]
    bids = [line.split(" ")[1] for line in lines if line != ""]

    results = []
    for hand, bid in zip(hands, bids):
        points = {key: 0 for key in CARDS_NAME}
        for card in hand:
            points[card] += 1
        mod_hand = modify_hand(hand)
        results.append([mod_hand, bid, get_score(points), hand])

    # [print(hand_point) for hand_point in results]
    results = np.array(results)
    print(np.sort(np.array(CARDS_NAME)))
    results = results[results[:, 0].argsort(kind='mergesort')]
    results = results[results[:, 2].argsort(kind='mergesort')]
    [print(result) for result in results]
    re = [np.int_(hand_point[1]) * (i+1) for i, hand_point in enumerate(results)]
    print(np.sum(re))


if __name__ == '__main__':
    main()