from itertools import product


## This is equal to the first problem, but we change the definitions of evaluate_operator and get_operators to include
## the new case. This takes longer, but not too much. This problem probably has a more intelligent solution
# finding factors of the result.

def evaluate_operator(a: int, b: int, operator: str):
    operations = {"+": a + b, "*": a * b, "|": int(str(a) + str(b))}
    return operations[operator]


def evaluate_result(numbers: list, operators: str):
    assert len(numbers) == len(operators) + 1, "The numbers and the operators don't match"
    result = int(numbers[0])
    for i in range(len(numbers) - 1):
        result = evaluate_operator(result, int(numbers[i + 1]), operators[i])

    return result


def get_operators(nb_operators):
    return [''.join(i) for i in product('+*|', repeat=nb_operators)]


def is_valid(result, numbers, operators):
    for op in operators:
        if result == evaluate_result(numbers, op):
            return True

    return False


if __name__ == '__main__':
    with open("input_day_7_1.txt", "r") as f:
        file = f.readlines()

    lines = [line.split("\n")[0] for line in file]
    results = [int(l.split(":")[0]) for l in lines]
    numbers = [l.split(":")[1].split(" ")[1:] for l in lines]
    operations = [get_operators(len(number) - 1) for number in numbers]

    total = 0
    for i in range(len(results)):
        if is_valid(results[i], numbers[i], operations[i]):
            total += results[i]

    print(total)
