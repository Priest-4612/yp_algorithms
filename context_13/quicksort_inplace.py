# https://contest.yandex.ru/contest/24735/run-report/55687014/
import random


def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = random.choice(array)
    less_values = [n for n in array if n < pivot]
    center_value = [pivot] * array.count(pivot)  # в целом лишний код.
    greater_value = [n for n in array if n > pivot]
    return quicksort(less_values) + center_value + quicksort(greater_value)


if __name__ == '__main__':
    count_participants = int(input())
    entries = [input().split() for _ in range(count_participants)]
    for index, value in enumerate(entries):
        entries[index] = (-int(value[1]), int(value[2]), value[0])
    for item in quicksort(entries):
        print(item[2])
