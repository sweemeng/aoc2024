from time import sleep

from IPython.lib.deepreload import original_import
from asciimatics.screen import ManagedScreen

HEADING = [(-1,0), (0,1), (1,0), (0,-1)]
HEADING_SYMBOL = ["^", ">", "v", "<"]
OUT_OF_BOUND = 1
GOES_IN_CIRCLE = 2


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


def solution(file_name, barrier=None, size=10):
    maps, guard = parse(file_name)
    heading = HEADING[0]
    tracks = set()
    last_count = 0
    while True:
        tracks.add(guard)
        if is_barrier(guard, heading, maps, sim_barrier=barrier):
            heading = turn(heading)

        guard = move(guard, heading)

        if out_of_map(guard, size=size):
            status = OUT_OF_BOUND
            print("Out of bound")
            break
        maps[guard] = "X"
        last_count = len(tracks)
    return tracks, status


def solution_2(file_name, tracks, size=10):
    track_list = list(tracks)
    count = 0
    while track_list:
        barrier = track_list.pop(0)
        tracks, sim_status = solution(file_name, barrier=barrier, size=size)
        if sim_status == GOES_IN_CIRCLE:
            count += 1
        else:
            continue
    print(count)


def solution_animate(file_name, size=10):
    # Do not use for actual solution, it will run out of buffer
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
            sleep(0.01)
            screen.clear()

def move(pos, heading):
    return pos[0] + heading[0], pos[1] + heading[1]


def turn(current_heading):
    i = HEADING.index(current_heading)
    return HEADING[(i + 1) % 4]


def is_barrier(guard, heading, maps, sim_barrier=None):
    next_pos = move(guard, heading)
    if sim_barrier:
        if sim_barrier == next_pos:
            return True
    if maps.get(next_pos, ".") == "#":
        return True

    return False


def out_of_map(pos, size):
    return pos[0] < 0 or pos[0] >= size or pos[1] < 0 or pos[1] >= size


if __name__ == "__main__":
    #solution_animate("day_06/test_data.txt")
    test_tracks, status = solution("day_06/test_data.txt", size=10)
    actual_tracks, actual_status = solution("day_06/actual_data.txt", size=130)
    solution_2("day_06/test_data.txt", test_tracks, size=10)
    #solution_2("day_06/actual_data.txt", actual_tracks, size=130)
    # 1816 too high