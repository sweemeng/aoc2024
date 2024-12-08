from itertools import product
from stringprep import b1_set


def parse(filename, answer_mode=False):
    maps = {}
    answer = {}
    with open(filename, "r") as file:
        row = 0
        for line in file:
            line = line.strip()
            col = 0
            for c in line:
                if c == ".":
                    col += 1
                    continue
                maps[(row, col)] = c
                if answer_mode:
                    if c == "#":
                        answer[(row, col)] = c
                col += 1
            row += 1
    return maps, answer


def distance(a, b):
    return (a[0] - b[0]), (a[1] - b[1])


def print_map(maps, answers, size=12):
    for i in range(size):
        for j in range(size):
            if (i, j) in maps:
                print(maps[(i, j)], end="")
            elif (i, j) in answers:
                print("#", end="")
            else:
                print(".", end="")
        print()


def solution(file_name, size=12):
    maps, answers = parse(file_name, answer_mode=True)
    answers2 = {}
    print_map(maps, answers, size)
    print("=====================================")
    antennas = list(set(maps.values()))
    print(antennas)
    for antenna in antennas:
        print(f"Antenna: {antenna}")
        for i in output_pairs(antenna, maps):
            print(i)
            antinodes = get_antinodes(i[0], i[1])
            print(antinodes)
            factor = 0
            while True:
                factor += 1
                antinodes2 = get_antinodes(i[0], i[1], factor=factor)
                if out_of_bounds(maps, antinodes2, size=size):
                    break
                answers2[antinodes2] = "#"
            answers[antinodes] = "#"
        print("=====================================")
    print(answers)
    inbound = [i for i in answers.keys() if not out_of_bounds(maps, i, size=size)]
    print("number of antinodes, ", len(inbound))
    print("adjusted antinodes,", len(answers2))
    print_map(maps, answers, size)
    print("Adjusted")
    print_map(maps, answers2, size)

def get_antinodes(a, b, factor=2):
    d = distance(a, b)
    print(d)
    d2 = (d[0] * factor) , (d[1] * factor)
    print(d2)
    return b[0] + d2[0], b[1] + d2[1]


def output_pairs(antenna, maps):
    coordinates = [i for i in maps if maps[i] == antenna]
    if len(coordinates) == 0:
        return []
    for i in product(coordinates, repeat=2):
        if i[0] != i[1]:
            yield i


def output_map(maps, size=12):
    result = ""
    for i in range(size):
        for j in range(size):
            if (i, j) in maps:
                result += maps[(i, j)]
            else:
                result += "."
        result += "\n"
    return result


def out_of_bounds(maps, pos, size=12):
    if pos[0] < 0 or pos[0] >= size:
        return True
    if pos[1] < 0 or pos[1] >= size:
        return True
    return False



if __name__ == "__main__":
    #solution("day_08/test_data.txt")
    solution("day_08/actual_data.txt", size=50)