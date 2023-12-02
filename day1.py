
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
NUMBERS_IN_LETTERS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
           "nine"]

def day1_0(lines):
    total = 0
    for line in lines:
        digits = [digit for digit in line if digit in NUMBERS]
        total += int(digits[0] + digits[-1])
    print(total)

def find_left_number(line):
    for i in range(len(line)):
        if line[i] in NUMBERS:
            return line[i]
        for j, number in enumerate(NUMBERS_IN_LETTERS):
            if number in line[:i + 1]:
                return str(j)

def find_right_number(line):
    for i in range(len(line)-1, -1, -1):
        if line[i] in NUMBERS:
            return line[i]
        for j, number in enumerate(NUMBERS_IN_LETTERS):
            if number in line[i:]:
                return str(j)

def day1_1(lines):
    total = 0
    for line in lines:
        total += int(find_left_number(line) + find_right_number(line))

    print(total)


def main():
    with open("input day1.txt") as f:
        lines = f.readlines()

    day1_1(lines)


if __name__ == '__main__':
    main()