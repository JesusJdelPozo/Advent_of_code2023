import numpy as np

def day6_0(lines):
    times = lines[0].split(":")[1].strip("\n").split(" ")
    times = [int(time) for time in times if time != ""]
    distances = lines[1].split(":")[1].split(" ")
    distances = [int(distance) for distance in distances if distance != ""]
    limit_times_plus = [(time + np.sqrt(time*time-4*distance))/2 for time, distance in zip(times, distances)]
    limit_times_minus = [(time - np.sqrt(time*time-4*distance))/2 for time, distance in zip(times, distances)]
    ways = 1
    for time_low, time_high in zip(limit_times_minus, limit_times_plus):
        if np.isclose(int(time_low), time_low):
            time_low += 1

        time_interval = int(time_high) - (int(time_low))
        ways *= time_interval

    return ways


def day6_1(lines):
    lines = [line.replace(" ", "") for line in lines]
    return day6_0(lines) + 1  # For some reason I don't understand


def main():
    with open("input day6.txt") as f:
        lines = f.readlines()

    print(day6_0(lines))
    print(day6_1(lines))


if __name__ == '__main__':
    main()