import re

if __name__ == '__main__':
    with open("input_day_3_1.txt", "r") as f:
        file = f.readlines()

    input_str = "".join(file)
    total_sum = 0
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, input_str)
    for match in matches:
        numbers = match[4:-1].split(',')
        x, y = int(numbers[0]), int(numbers[1])
        total_sum += x * y

    print(total_sum)
