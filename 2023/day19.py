from typing import List
from collections import defaultdict
import numpy as np


def match_case(case: str, part: List[int]):
    x, m, a, s = part
    cases = case.split(",")
    for case in cases:
        command = case.split(":")
        if len(command) == 2:
            if eval(command[0]):
                return command[1]
        else:
            return command[0]


def process_part(workflows, workflow_name, part):
    c = match_case(workflows[workflow_name], part)
    if c == "A":
        return "A", sum(part)
    elif c == "R":
        return "R", 0
    else:
        return process_part(workflows, c, part)


def retrive_data(lines):
    flag = True
    workflow = {}
    parts = []
    for line in lines:
        line = line.strip("\n")

        if line == "":
            flag = False

        if flag:
            key = line.split("{")[0]
            value = line.split("{")[1].strip("}")
            workflow[key] = value
        elif flag == False and line != "":
            part = line.strip("{").strip("}").split(",")
            values = [int(p.split("=")[1]) for p in part]
            parts.append(values)

    return parts, workflow


def compress(workflow):
    compressed = {}
    for key, value in workflow.items():
        cases = value.split(",")
        new_cases = {}
        for case in cases:
            ini = 0
            fini = 0
            if ":" not in case:
                next_case = case
                if next_case in new_cases.keys():
                    ini2, fini2 = new_cases[next_case]
                    new_cases[next_case] = (ini2, fini2, ini, fini)
                else:
                    new_cases[next_case] = (ini, fini)
                continue
            else:
                next_case = case.split(":")[1]

            number = int(case.split(":")[0][2:])
            if case[0:2] == "x<":
                ini = 0
                fini = number
            if case[0:2] == "x>":
                ini = number
                fini = 4000

            if case[0:2] == "m<":
                ini = 4000
                fini = 4000 + number
            if case[0:2] == "m>":
                ini = 4000 + number
                fini = 8000

            if case[0:2] == "a<":
                ini = 8000
                fini = 8000 + number
            if case[0:2] == "a>":
                ini = 8000 + number
                fini = 12000

            if case[0:2] == "s<":
                ini = 12000
                fini = 12000 + number

            if case[0:2] == "s>":
                ini = 12000 + number
                fini = 16000

            new_cases[next_case] = (ini, fini)
        compressed[key] = new_cases

    return compressed


def find_ranges(workflow, start, path=None, parent=None):
    if path is None:
        path = defaultdict(list)
        parent = (start,)

    for key, value in workflow[start].items():
        if key == "A":
            path[parent].append(("A", value))
        elif key == "R":
            path[parent].append(("R", value))
        elif key in workflow.keys():
            path[parent + (key,)].append(value)
            find_ranges(workflow, key, path, parent + (key,))

    return path


def find_ranges2(workflow, start, ranges, path=None, parent=None):
    if path is None:
        path = defaultdict(list)
        parent = (start,)
    if start == "A":
        return ranges, "A"
    elif start == "R":
        return ranges, "R"

    next_jobs = workflow[start]
    next_keys = [k for k in next_jobs.keys()]
    rest =ranges.copy()
    for key in next_keys:
        to_key = rest.copy()
        range_key, r = next_jobs[key]
        print(range_key, r)
        if isinstance(range_key, tuple):
            range_key, r = range_key
        print(r[1], r[0])
        consumed = r[1] - r[0]
        if range_key in rest.keys():
            val = rest[range_key]
            if val > consumed:
                to_key[range_key] = consumed
                rest[range_key] = val - consumed
            else:
                to_key[range_key] = val
                rest[range_key] = 0
        else:
            to_key = rest.copy()
        # print("TO KEYS", ranges, to_key, rest)
        rangea = find_ranges2(workflow, key, to_key)
        path[start].append(rangea)

    return path


def parse(workflow):
    compressed = {}
    for key, value in workflow.items():
        cases = value.split(",")
        new_cases = {}
        for case in cases:
            ini = 0
            fini = 0
            if ":" not in case:
                next_case = case
                if next_case in new_cases.keys():
                    inner_tuple = new_cases[next_case]
                    inner_list = [inner_tuple, (case, (ini, fini))]
                    new_cases[next_case] = inner_list
                else:
                    new_cases[next_case] = (case, (ini, fini))
                continue
            else:
                next_case = case.split(":")[1]

            number = int(case.split(":")[0][2:])
            if case[0:2] == "x<":
                ini = 0
                fini = number
            if case[0:2] == "x>":
                ini = number
                fini = 4000

            if case[0:2] == "m<":
                ini = 0
                fini = number
            if case[0:2] == "m>":
                ini = number
                fini = 4000

            if case[0:2] == "a<":
                ini = 0
                fini = number
            if case[0:2] == "a>":
                ini = number
                fini = 4000

            if case[0:2] == "s<":
                ini = 0
                fini = number

            if case[0:2] == "s>":
                ini = number
                fini = 4000

            new_cases[next_case] = (case[0], (ini, fini))
        compressed[key] = new_cases

    return compressed


def main():
    with open("test input.txt") as f:
        lines = f.readlines()

    parts, workflow = retrive_data(lines)
    # results = [process_part(workflow, "in", part) for part in parts]
    # print("Part 1 result = ", sum([result[1] for result in results]))
    ranges = {"x": 4000, "m": 4000, "a": 4000, "s": 4000}
    parsed_work = parse(workflow)
    print(parsed_work)
    ranges = find_ranges2(parsed_work, "in", ranges)
    [print(k, v) for k,v in ranges.items()]


#     compresed_workflows = compress(workflow)
#     a = find_ranges(compresed_workflows, "in")
#     [print(c, v) for c, v in compresed_workflows.items()]
#     [print(a, v) for a, v in a.items()]
#
#     ranges = np.zeros(16000, dtype=bool)
#     for key, value in a.items():
#         print(key)
#         for v in value:
#             if v[0] == "A":
#                 ini = v[1][0]
#                 fini = v[1][1]
#                 ranges[ini: fini] = 1
#             elif v[0] == "R":
#                 ini = v[1][0]
#                 fini = v[1][1]
#                 ranges[ini: fini] = 0
#             else:
#                 ini = v[0]
#                 fini = v[1]
#                 ranges[ini: fini] = 1
# #2754 4000 2006 2581
#
#     x = ranges[:4000]
#     m = ranges[4000:8000]
#     a = ranges[8000:12000]
#     s = ranges[12000:16000]
#     r2 = []
#     r = 0
#     for i in range(16000):
#         if ranges[i] == True:
#             r += 1
#         else:
#             if r != 0:
#                 r2.append((i, r))
#             r = 0
#
#     r2.append((i, r))
#     print(r2)
#
#     print(len(x[x == True]), len(m[m == True]), len(a[a == True]), len(s[s == True]))


if __name__ == '__main__':
    main()
