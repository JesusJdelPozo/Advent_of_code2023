import re

if __name__ == '__main__':
    with open("input_day_3_1.txt", "r") as f:
        file = f.readlines()

    input_str = "".join(file)
    to_do = input_str.split("do()")
    total_sum = 0
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    for string in to_do:
        doing_string = string.split("don't()")[0]
        matches = re.findall(pattern, doing_string)
        for match in matches:
            numbers = match[4:-1].split(',')
            x, y = int(numbers[0]), int(numbers[1])
            total_sum += x * y

    print(total_sum)
