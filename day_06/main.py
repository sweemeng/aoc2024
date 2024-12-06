from time import sleep

from asciimatics.screen import ManagedScreen

HEADING = [(-1,0), (0,1), (1,0), (0,-1)]
HEADING_SYMBOL = ["^", ">", "v", "<"]


def parse(filename):
    maps = {}
    with open(filename, "r") as file:
        row = 0
        guard_start = None
        for line in file:
            line = line.strip()
            col = 0
            for c in line:
                if c == "#":
                    maps[(row, col)] = c
                if c == "^":
                    guard_start = (row, col)
                col += 1
            row += 1
    return maps, guard_start


def print_map(maps, guard, guard_heading, size=10):
    heading_index = HEADING.index(guard_heading)
    symbol = HEADING_SYMBOL[heading_index]
    for i in range(size):
        for j in range(size):
            if (i, j) in maps:
                print("#", end="")
            elif (i, j) == guard:
                print(symbol, end="")
            else:
                print(".", end="")

        print()


def print_map_string(maps, guard, guard_heading, size=10):
    heading_index = HEADING.index(guard_heading)
    symbol = HEADING_SYMBOL[heading_index]
    result = ""
    for i in range(size):
        for j in range(size):
            if (i, j) == guard:
                result += symbol
            elif (i, j) in maps:
                if maps[(i, j)] == "#":
                    result += "#"
                elif maps[(i, j)] == "X":
                    result += "X"
            else:
                result += "."

        result += "\n"
    return result


def solution(file_name, size=10):
    maps, guard = parse(file_name)
    heading = HEADING[0]
    tracks = set()
    while True:
        if is_barrier(guard, heading, maps):
            heading = turn(heading)

        guard = move(guard, heading)

        if out_of_map(guard, size=size):
            break
        tracks.add(guard)
        maps[guard] = "X"
    print(len(tracks))


def solution_animate(file_name, size=10):
    maps, guard = parse(file_name)
    heading = HEADING[0]
    map_str = print_map_string(maps, guard, heading, size=size)
    screen_start = (0, 0)
    tracks = set()
    with ManagedScreen() as screen:
        while True:
            temp = map_str.split("\n")
            for i, t in enumerate(temp):
                screen.print_at(t, *screen_start)
                screen_start = (screen_start[0], screen_start[1]+1)
            screen_start = (0, 0)
            screen.print_at(map_str, *screen_start)
            if is_barrier(guard, heading, maps):
                heading = turn(heading)

            guard = move(guard, heading)

            if out_of_map(guard, size=size):
                break
            tracks.add(guard)
            maps[guard] = "X"
            map_str = print_map_string(maps, guard, heading, size=size)

            screen.refresh()
            sleep(0.1)
            screen.clear()
    print(len(tracks))


def move(pos, heading):
    return pos[0] + heading[0], pos[1] + heading[1]


def turn(current_heading):
    i = HEADING.index(current_heading)
    return HEADING[(i + 1) % 4]


def is_barrier(guard, heading, maps):
    next_pos = move(guard, heading)
    if maps.get(next_pos, ".") == "#":
        return True
    return False


def out_of_map(pos, size):
    return pos[0] < 0 or pos[0] >= size or pos[1] < 0 or pos[1] >= size


if __name__ == "__main__":
    #solution_animate("day_06/test_data.txt")
    solution("day_06/test_data.txt", size=10)
    solution_animate("day_06/actual_data.txt", size=130)
    # 4818 too low