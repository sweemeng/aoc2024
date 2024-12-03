from copy import deepcopy

INCREASING = -1
DECREASING = 1
NEUTRAL = 0
DEBUG = False


def loader(data_file):
    with open(data_file, "r") as f:
        lines =  f.read().strip().split("\n")
        for line in lines:
            yield [int(i) for i in line.split()]


def solution(data_file, debug=False, triggered=False):
    data = loader(data_file)
    safe_count = 0

    for row in data:
        check = check_data(row, triggered=triggered)
        if debug:
            print("Row", row)
            print("Check", check)
        if check:
            safe_count += 1
    print(safe_count)


def check_data(row, triggered=False):
    diffs = []

    for i in range(len(row) - 1):
        diffs.append(row[i] - row[i+1])
    check_1 = all([i in range(1, 4) for i in diffs])
    check_2 = all([i in range(-3, 0) for i in diffs])
    safe = check_1 or check_2
    if not safe and not triggered:
        for i in range(len(row)):
            new_row = deepcopy(row)
            new_row.pop(i)
            safe = check_data(new_row, triggered=True)
            if safe:
                break
    return safe


if __name__ == "__main__":
    solution("day_02/test_data.txt", triggered=True)
    solution("day_02/actual_data.txt", triggered=True)
    solution("day_02/test_data.txt")
    solution("day_02/actual_data.txt")

    # Current answer part 2, too low 337 not 348
