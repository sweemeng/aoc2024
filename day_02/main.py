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


def solution(data_file, safety=False, debug=False, failed_only=False):
    data = loader(data_file)
    safe_count = 0

    for row in data:
        check = check_data(row, debug=debug)
        if debug:
            print("Row", row)
            print("Check", check)
        if check:
            safe_count += 1
    print(safe_count)


def check_data(row, debug=DEBUG):
    safe = True
    trend = None
    copies = deepcopy(row)
    while copies:
        if debug:
            print(copies)
        if len(copies) == 1:
            break
        d1 = copies.pop(0)
        d2 = copies.pop(0)
        if trend is None:
            trend = get_trend(d1, d2)
        safe = is_data_safe(d1, d2, trend, debug=debug)
        if not safe:
            break
        trend = get_trend(d1, d2)
        copies.insert(0, d2)
    return safe


def is_data_safe(num_1, num_2, trends, debug=False):
    safe = True
    trend = get_trend(num_1, num_2)
    if debug:
        print("num 1", num_1)
        print("num 2", num_2)
        print("Trend", trend)
    if trend == NEUTRAL:
        if debug:
            print("trend cannot be zero")
        return False
    if trend != trends and trends is not None:
        if debug:
            print("Trend mismatch")
        safe = False

    diff = abs(num_1 - num_2)
    if debug:
        print("Diff of", num_1, num_2, "is", diff)
    if diff not in range(1, 4):
        if debug:
            print("Diff not in range", diff)
        safe = False
    return safe


def get_trend(num_1, num_2):
    diff = num_1 - num_2
    if diff == 0:
        return NEUTRAL
    return abs(diff)/diff


if __name__ == "__main__":
    solution("day_02/test_data.txt", debug=True)
    solution("day_02/actual_data.txt")
    # Current answer part 2, too low 337
