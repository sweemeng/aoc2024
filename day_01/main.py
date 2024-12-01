from collections import Counter

def extract_data(data_file):
    l = []
    r = []
    with open(data_file, 'r') as f:
        data = f.read().strip()
        for line in data.split('\n'):
            x,y = line.split()
            l.append(int(x))
            r.append(int(y))
    return l, r

def solution_1(data_file):
    l, r = extract_data(data_file)
    ds = []
    for i in range(len(l)):
        ds.append(abs(l[i]-r[i]))
    print(sum(ds))


def solution_2(data_file):
    l, r = extract_data(data_file)
    counter = Counter(r)
    results = []
    for i in l:
        results.append(counter[i]* i)
    print(sum(results))


if __name__ == '__main__':
    # test_mode
    solution_1("day_01/test_data.txt")
    solution_1("day_01/actual_data.txt")
    solution_2("day_01/test_data.txt")
    solution_2("day_01/actual_data.txt")