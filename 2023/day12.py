import numpy as np
from itertools import combinations
from time import perf_counter


def filter(target, test):
    print(target)
    res = target.lstrip(".")
    print(res)
    res = res.rstrip(".")
    print(res, test)
    val = test.copy()
    filtered = target.split(".")
    filtered = [t for t in filtered if t != ""]
    print("filtered", filtered, test)
    for filter in filtered:
        for t in test:
            print(filter, t)
            if filter == t * "#":
                res = res.replace(t * "#", "")
                if t in val:
                    val = np.delete(val, t)
    print("filtered equal", res, val)
    return res, val


def generate_comb(spring, validator):
    filter(spring, validator)
    strings = [v * "#" + "." for v in validator]
    strings[-1] = strings[-1][:-1]
    # print(strings)
    # print(strings)
    ndots = len(spring) - sum([len(val) for val in strings])
    dots = ["." for _ in range(ndots)]
    print(ndots, len(spring), spring, strings, dots)
    if len(strings) >= ndots:
        base = strings
        group = dots
    else:
        base = dots
        group = strings
    results = []
    # [print(comb, len(dots), len(strings)) for comb in combinations(range(len(dots)+1), len(strings)+1)]
    # print(dots, strings)
    for comb in combinations(range(len(dots)+1), len(strings)+1):
        # print(comb)
        res = ["."] * (len(dots) + len(strings))
        ini = 0
        for i, j in enumerate(comb):
            if ini < j:
                res[ini:j] = "."
            res[ini:j] = strings[i]
            # print(res[ini:j])
            ini = j
            # print(res, res[j], ini, j)
        res = "".join(res)
        # print(res, spring, validate(res, spring))
        if validate(res, spring):
            results.append(res)
    # for group_indx in combinations(range(len(base)+len(group)), len(group)):
    #     # print(f"{group_indx=}", spring, len(base), len(group))
    #     res = ""
    #     gdx = 0
    #     bdx = 0
    #     for k in range(len(base)+len(group)):
    #         # print("block", k, len(base)+len(group), gdx, bdx)
    #         if k in group_indx:
    #             res += group[gdx]
    #             # print("went to group ading",group[gdx],"to the result:",res)
    #             gdx += 1
    #         else:
    #             res += base[bdx]
    #             # print("went to base ading",base[bdx],"to the result:", res)
    #             bdx += 1
    #
    #     # print(res, spring, validate(res, spring), "group", gdx, "base", bdx)
    #     if validate(res, spring):
    #         results.append(res)
    # print("result for spring: ", spring, results)
    return results


def validate(test, spring):
    if len(test) != len(spring):
        print(test, spring)
        print("WTF")

    for i in range(len(spring)):
        if spring[i] != "?":
            if spring[i] != test[i]:
                return False
    return True


def main():
    with open("input day12.txt") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines if line != ""]
    springs = [line.split(" ")[0] for line in lines]
    errors = [line.split(" ")[1] for line in lines]
    error_lists = [np.int_(error.split(",")) for error in errors]
    generate_comb(springs[1], error_lists[1])
    t1= perf_counter()
    results1 = [generate_comb(spring, error) for spring, error in zip(springs, error_lists)]
    print(perf_counter() - t1)
    # print([len(res) for res in results1])
    # unfolded_errors = [2 * (error + ",") for error in errors]
    # unfolded_errors = [np.int_(error[:-1].split(",")) for error in unfolded_errors]
    # unfolded_springs = [(spring + "?" + spring) for spring in springs]
    # t1= perf_counter()
    # results2 = [generate_comb(spring, error) for spring, error in zip(unfolded_springs, unfolded_errors)]
    # print(perf_counter() - t1)
    # print([len(res) for res in results2])
    # unfolded_errors = [3 * (error + ",") for error in errors]
    # unfolded_errors = [np.int_(error[:-1].split(",")) for error in unfolded_errors]
    # unfolded_springs = [(spring + "?" + spring + "?" + spring) for spring in springs]
    # results3 = [generate_comb(spring, error) for spring, error in zip(unfolded_springs, unfolded_errors)]
    # print([len(res) for res in results3])
    # unfolded_springs = [("%" + spring +"%"+ spring) for spring in springs]
    # results2 = [generate_comb(spring, error) for spring, error in zip(unfolded_springs, unfolded_errors)]
    # print([len(res) for res in results2])
    # unfolded_springs = [("%" + spring +"%"+ spring) for spring in springs]
    # results2 = [generate_comb(spring, error) for spring, error in zip(unfolded_springs, unfolded_errors)]
    # print([len(res) for res in results2])
    result12 = []
    for r1,r2 in zip(results1, results2):
        lenr1 = np.int64(len(r1))
        lenr2 = np.int64(len(r2))
        result12.append(lenr2/lenr1)

    print(result12)


#91675959800158 toolow
#127518498916309 toolow!!!

if __name__ == '__main__':
    main()