def make_map(filename):
    maps = {}
    x, y = 0, 0
    with open(filename) as f:
        for line in f:
            for char in line:
                if char == '\n':
                    x = 0
                    y += 1
                else:
                    maps[(x, y)] = char
                    x += 1
    return maps


def print_map(maps, size=10):
    for y in range(size):
        for x in range(size):
            print(maps[(x, y)], end='')
        print()


def get_vertical_line(maps, x, y, size=10):
    # get only 4 points
    points = []
    for i in range(4):
        if y+i >= size:
            continue
        points.append((x, y+i))
    return points


def get_horizontal_line(maps, x, y, size=10):
    # get only 4 points
    points = []
    for i in range(4):
        if x+i >= size:
            continue
        points.append((x+i, y))
    return points


def get_diagonal_line(maps, x, y, size=10, x_mode=False):
    # get only 4 points
    points = []
    if x_mode:
        length = 3
    else:
        length = 4
    for i in range(length):
        if x+i >= size or y+i >= size:
            continue
        points.append((x+i, y+i))
    return points


def get_diagonal_line_reverse(maps, x, y, size=10, x_mode=False):
    # get only 4 points
    points = []
    if x_mode:
        length = 3
    else:
        length = 4
    for i in range(length):
        if x+i >= size or y-i < 0:
            continue
        points.append((x+i, y-i))
    return points


def check_line(maps, points, x_mode=False):
    result = []
    if x_mode:
        value = "MAS"
    else:
        value = "XMAS"
    for point in points:
        result.append(maps[point])
    t = ''.join(result)
    r = t[::-1]
    if t == value or r == value:
        return True
    return False




def solution(maps, size=10, debug=False):
    count = 0
    new_maps = {}
    for y in range(size):
        for x in range(size):
            new_maps[(x, y)] = "."

    for y in range(size):
        for x in range(size):

            vertical_line = get_vertical_line(maps, x, y, size)
            horizontal_line = get_horizontal_line(maps, x, y, size)
            diagonal_line = get_diagonal_line(maps, x, y, size)
            diagonal_line_reverse = get_diagonal_line_reverse(maps, x, y, size)
            if check_line(maps, vertical_line):
                count += 1
                for vl in vertical_line:
                    new_maps[vl] = maps[vl]
            if check_line(maps, horizontal_line):
                count += 1
                for hl in horizontal_line:
                        new_maps[hl] = maps[hl]
            if check_line(maps, diagonal_line):
                count += 1
                for dl in diagonal_line:
                    new_maps[dl] = maps[dl]
            if check_line(maps, diagonal_line_reverse):
                count += 1
                for dr in diagonal_line_reverse:
                    new_maps[dr] = maps[dr]
    if debug:
        print_map(new_maps, size)
    print(count)


def solution_2(maps, size=10, debug=False):
    count = 0
    new_maps = {}
    for y in range(size):
        for x in range(size):
            new_maps[(x, y)] = "."

    for y in range(size):
        for x in range(size):
            if y + 2 >= size:
                continue
            diagonal_line = get_diagonal_line(maps, x, y, size, x_mode=True)
            reverse_diagonal_line = get_diagonal_line_reverse(maps, x, y+2, size, x_mode=True)

            check_1 = check_line(maps, diagonal_line, x_mode=True)
            check_2 = check_line(maps, reverse_diagonal_line, x_mode=True)
            if debug:
                print(x, y)
                print(check_1, diagonal_line)
                print(check_2, reverse_diagonal_line)
            if check_1 and check_2:
                count += 1
                for dl in diagonal_line:
                    new_maps[dl] = maps[dl]
                for dr in reverse_diagonal_line:
                    new_maps[dr] = maps[dr]
    if debug:
        print_map(new_maps, size)
    print(count)



def main():
    maps = make_map('day_04/test_data.txt')
    print_map(maps)

    print("----")
    solution(maps, 10)
    maps_actual = make_map('day_04/actual_data.txt')
    print_map(maps_actual, 140)

    print("----")
    solution(maps_actual, 140)

    print("----")
    solution_2(maps, 10, debug=True)
    print("----")
    solution_2(maps_actual, 140, debug=False)


if __name__ == '__main__':
    main()