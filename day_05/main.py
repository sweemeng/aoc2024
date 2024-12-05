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

def solution(filename):
    rules, manuals = parse(filename)
    correct_pages = []
    for pages in manuals:
        pages_check = []
        for page in pages:
            pages_check.append(check_rules(page, rules, pages))
        if all(pages_check):
            print("Manual is correct", pages)
            correct_pages.append(pages)
    print(rules)
    print(manuals)
    results = []

    for pages in correct_pages:
        middle = int(len(pages) / 2)
        print(pages[middle])
        results.append(pages[middle])
    print(sum(results))


if __name__ == "__main__":
    solution("day_05/test_data.txt")
    solution("day_05/actual_data.txt")