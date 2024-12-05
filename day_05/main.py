from copy import deepcopy


def parse(filename):
    rules = {}
    manuals = []
    with open(filename) as f:
        for line in f:
            if "|" in line:
                key, value = line.strip().split("|")
                key = int(key.strip())
                value = int(value.strip())
                if not key in rules:
                    rules[key] = []
                rules[key].append(value)
            elif "," in line:
                pages = line.strip().split(",")
                pages = [int(page.strip()) for page in pages]
                manuals.append(pages)
            else:
                continue
    return rules, manuals


def check_rules(page, rules, pages, debug=False):
    page_index = pages.index(page)
    if not page in rules:
        return True
    rule = rules[page]
    rule_pages = []

    for rule_page in rule:
        if rule_page in pages:
            rule_pages.append(pages.index(rule_page))
    for rule_page in rule_pages:
        if rule_page < page_index:
            if debug:
                print("Break rule", page, rule, pages)

            return False
    return True

def solution(filename, debug=False):
    rules, manuals = parse(filename)
    correct_pages = []
    wrong_pages = []
    for pages in manuals:
        pages_check = []
        for page in pages:
            check_value = check_rules(page, rules, pages, debug=debug)
            pages_check.append(check_value)
        if all(pages_check):
            print("Manual is correct", pages)
            correct_pages.append(pages)
        else:
            print("Manual is wrong", pages)
            new_pages = rearrange_pages(pages, rules, debug=debug)
            print("Corrected manual", new_pages)
            wrong_pages.append(new_pages)

    results = []

    for pages in correct_pages:
        middle = int(len(pages) / 2)
        results.append(pages[middle])
    print(sum(results))
    wrong_results = []
    for pages in wrong_pages:
        middle = int(len(pages) / 2)
        wrong_results.append(pages[middle])
    print(sum(wrong_results))


def rearrange_pages(pages, rules, debug=False):
    new_pages = deepcopy(pages)
    all_correct = False
    ptr = 0
    while not all_correct:
        if ptr >= len(new_pages):
            break
        copies = deepcopy(new_pages)
        new_pages = []
        page = copies[ptr]
        check = check_rules(page, rules, copies, debug=debug)
        if check:
            if ptr:
                new_pages.extend(copies[:ptr])

            new_pages.extend(copies[ptr:])
            ptr += 1
        else:
            new_pages.extend(copies[:ptr-1])
            new_pages.append(copies[ptr])
            new_pages.append(copies[ptr-1])
            new_pages.extend(copies[ptr+1:])
            ptr = 0 # just recheck again
        checks = []
        for i in range(len(copies)):
            page = copies[i]
            check = check_rules(page, rules, copies)
            checks.append(check)
        all_correct = all(checks)
    return new_pages


if __name__ == "__main__":
    solution("day_05/test_data.txt", debug=True)
    solution("day_05/actual_data.txt")