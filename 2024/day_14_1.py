import numpy as np


if __name__ == '__main__':
    with open("input_day_14.txt", "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines if line != ""]
    shape = (103, 101)

    # test_shape = (7, 11)
    # test = ["p=0,4 v=3,-3"
    #         ,"p=6,3 v=-1,-3"
    #         ,"p=10,3 v=-1,2"
    #         ,"p=2,0 v=2,-1"
    #         ,"p=0,0 v=1,3"
    #         ,"p=3,0 v=-2,-2"
    #         ,"p=7,6 v=-1,-3"
    #           ,"p=3,0 v=-1,-2"
    #           ,"p=9,3 v=2,3  "
    #           ,"p=7,3 v=-1,2 "
    #           ,"p=2,4 v=2,-3 "
    #          ,"p=9,5 v=-3,-3"]
    #
    # lines = test
    # shape = test_shape

    positions = [(int(line.split("=")[1].split(" ")[0].split(",")[1]), int(line.split("=")[1].split(" ")[0].split(",")[0])) for line in lines if line != ""]
    velocities = [(int(line.split("=")[2].split(",")[1]), int(line.split("=")[2].split(",")[0])) for line in lines if line != ""]

    positions = np.array(positions)
    velocities = np.array(velocities)
    shape = np.array(shape)
    time = 100
    bath = np.zeros(shape, dtype=int)
    for position, velocity in zip(positions, velocities):
        new_position = position + velocity * time
        new_position = np.mod(new_position, shape)
        bath[*new_position] += 1

    print(bath)
    security_factor = np.sum(bath[:shape[0]//2, :shape[1]//2])           #  top_left
    security_factor *= np.sum(bath[shape[0]//2 + 1:, :shape[1]//2])      #  bottom_left
    security_factor *= np.sum(bath[:shape[0]//2, shape[1]//2 + 1:])      #  bottom_right
    security_factor *= np.sum(bath[shape[0]//2 + 1:, shape[1]//2 + 1:])  #  top_right
    print(security_factor)


