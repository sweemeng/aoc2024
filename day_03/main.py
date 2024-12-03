import re


def solution(line):
    re_pattern = r"(?P<ops>mul)\((?P<d1>\d+),(?P<d2>\d+)\)"
    print(sum([int(d1) * int(d2) for _, d1, d2 in re.findall(re_pattern, line)]))
    print(re.findall(re_pattern, line))

def solution_2(line):
    register = {}
    re_pattern = r"(?P<ops>mul)\((?P<d1>\d+),(?P<d2>\d+)\)"
    for matched in re.finditer(re_pattern, line):
        register[matched.start()] = matched.groupdict()
    disable_pattern = r"(?P<ops>don't\(\))"
    for matched in re.finditer(disable_pattern, line):

        register[matched.start()] = matched.groupdict()
    enable_pattern = r"(?P<ops>do\(\))"
    for matched in re.finditer(enable_pattern, line):
        register[matched.start()] = matched.groupdict()
    multiply_machine(register)

def multiply_machine(register):
    ordering = sorted(register.keys())
    results = []
    print(register)
    ops_toggle = True
    for i in ordering:
        if register[i]["ops"] == "mul":
            if ops_toggle:
                print("Multiplying", register[i]["d1"], register[i]["d2"])
                results.append(int(register[i]["d1"]) * int(register[i]["d2"]))
            else:
                print("Skipping", register[i]["d1"], register[i]["d2"])
        elif register[i]["ops"] == "don't()":
            ops_toggle = False
        elif register[i]["ops"] == "do()":
            ops_toggle = True
    print(sum(results))



def main():
    test_data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    solution(test_data)
    actual_data = open("day_03/actual_data.txt").read()
    solution(actual_data)
    test_data_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    solution_2(test_data_2)
    solution_2(actual_data)


if __name__ == "__main__":
    main()