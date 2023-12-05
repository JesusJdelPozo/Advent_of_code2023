import numpy as np

def day_4_0_and_1(lines):
    winnings = [line.split(":")[1].split("|")[0].split(" ") for line in lines]
    hands = [line.split(":")[1].split("|")[1].strip("\n").split(" ") for line in lines]
    cards = [card for hand in hands for card in hand if card != ""]
    cards_per_hand = 25
    points = []
    total_cards = np.ones(len(winnings), dtype=np.int32)
    for i, win in enumerate(winnings):
        p = 1
        wc = 0
        for j in range(cards_per_hand):
            if cards[i * cards_per_hand + j] in win:
                wc += 1
                p *= 2

        for k in range(wc):
            if i+k+1 < len(winnings):
                total_cards[i+k+1] += total_cards[i]

        points.append(p//2)

    print("total cards", np.sum(total_cards))
    print("total points", sum(points))

def main():
    with open("input day4.txt") as f:
        lines = f.readlines()

    day_4_0_and_1(lines)


if __name__ == '__main__':
    main()
