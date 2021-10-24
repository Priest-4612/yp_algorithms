# https://contest.yandex.ru/contest/23390/run-report/54696537/
from collections import Counter


def trainer(k, rows):
    counters = Counter(rows)
    return sum([1 for x in counters.values() if x <= 2 * k])


if __name__ == '__main__':
    ROW_LENGTH = 4
    k = int(input())
    rows = [int(x) for _ in range(ROW_LENGTH) for x in input() if x != '.']
    print(trainer(k, rows))
