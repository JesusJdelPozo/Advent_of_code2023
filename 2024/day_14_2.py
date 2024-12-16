import matplotlib.pyplot as plt
import numpy as np


def get_final_bath(time):
    bath = np.zeros(shape, dtype=int)
    for position, velocity in zip(positions, velocities):
        new_position = position + velocity * time
        new_position = np.mod(new_position, shape)
        bath[*new_position] += 1
    return bath


if __name__ == '__main__':
    with open("input_day_14.txt", "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines if line != ""]
    shape = (103, 101)
    positions = [
        (int(line.split("=")[1].split(" ")[0].split(",")[1]), int(line.split("=")[1].split(" ")[0].split(",")[0])) for
        line in lines if line != ""]
    velocities = [(int(line.split("=")[2].split(",")[1]), int(line.split("=")[2].split(",")[0])) for line in lines if
                  line != ""]

    positions = np.array(positions)
    velocities = np.array(velocities)
    shape = np.array(shape)
    initial_bath = get_final_bath(0)
    iterations = 1
    tree = np.zeros(shape)
    for i, row in enumerate(range(tree.shape[0])):
        tree[i, tree.shape[1]//2 - i: tree.shape[1]//2 + i + 1] = 1

    dist = 10000000000000000000000
    best_match = -1
    while True:
        new_bath = get_final_bath(iterations)
        dist_new = np.sum(np.abs(tree - new_bath))
        if dist_new < dist:
            dist = dist_new
            best_match = iterations
        if (new_bath == initial_bath).all():
            break
        iterations += 1

    print(iterations)
    print(best_match, dist)
    bath = get_final_bath(best_match)
    plt.imshow(bath)
    plt.show()
