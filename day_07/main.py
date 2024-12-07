from itertools import product

NOOP = 0
ADD = 1
MUL = 2
CONCAT = 3

def parse(filename):
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            answer, values = line.split(":")
            values = values.split(" ")
            values = [int(v) for v in values if v]
            answer = int(answer)
            yield answer, values


def runner(values):
    ops_len = len(values) - 1
    for ops in product([ADD, MUL], repeat=ops_len):

        registers = list(zip(ops, values[1:]))
        registers.insert(0, (NOOP, values[0]))
        yield machine(registers)


def concat_runner(values):
    ops_len = len(values) - 1
    for ops in product([ADD, MUL, CONCAT], repeat=ops_len):

        registers = list(zip(ops, values[1:]))
        registers.insert(0, (NOOP, values[0]))
        yield machine(registers)


def machine(registers):
    totals = 0
    for ops, value in registers:
        if ops == NOOP:
            totals = value
        elif ops == ADD:
            totals += value
        elif ops == MUL:
            totals *= value
        elif ops == CONCAT:
            totals = totals * 10 + value
    return totals


def solution(filename):
    correct = set()
    concat_correct = set()
    for test_values, operations in parse(filename):
        result = runner(operations)
        for r in result:
            if r == test_values:
                correct.add(test_values)
    print(correct)
    print(sum(list(correct)))
    concat_total = 0
    for test_values, operations in parse(filename):
        result = concat_runner(operations)
        for r in result:
            if r == test_values:
                if test_values not in concat_correct:
                    concat_total += test_values
                concat_correct.add(test_values)
    print(concat_correct)
    #print(sum(list(concat_correct)))
    print(concat_total)
    # 9440677114706 too low



if __name__ == "__main__":
    solution("day_07/test_data.txt")
    solution("day_07/actual_data.txt")
