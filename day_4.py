from itertools import groupby

data = "168630-718098"


def is_valid(string: str) -> bool:
    if any(before > after for before, after in zip(string, string[1:])):
        return False

    if not any(s == string[i + 1] for i, s in enumerate(string[:-1])):
        return False

    return True


def is_valid_2(string: str) -> bool:
    groups = tuple((i, len(tuple(g))) for i, g in groupby(string))

    if any(before > after for before, after in zip(string, string[1:])):
        return False

    if not any(g[1] == 2 for g in groups):
        return False

    return True


def part1():
    print('111111:', is_valid('111111'))
    print('223450:', is_valid('223450'))
    print('123789:', is_valid('111111'))
    start, end = map(int, data.split('-'))
    print("Part 1's answer:", sum(is_valid(i) for i in map(str, range(start, end + 1))))


def part2():
    print('112233:', is_valid_2('112233'))
    print('123444:', is_valid_2('123444'))
    print('111122:', is_valid_2('111122'))
    print('788999:', is_valid_2('788999'))
    start, end = map(int, data.split('-'))
    print("Part 2's answer:", sum(is_valid_2(i) for i in map(str, range(start, end + 1))))


def main():
    part1()
    part2()


main()
