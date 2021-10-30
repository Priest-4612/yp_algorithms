# https://contest.yandex.ru/contest/24735/run-report/55705349/
import random


def quicksort(array):

    def quicksort_inplace(array, start, end):
        if start >= end:
            return
        i, j = start, end
        pivot = array[random.randint(start, end)]
        while i <= j:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i, j = i + 1, j - 1
        quicksort_inplace(array, start, j)
        quicksort_inplace(array, i, end)

    start = 0
    end = len(array) - 1
    quicksort_inplace(array, start, end)
    return array


if __name__ == '__main__':
    count_participants = int(input())
    entries = [input().split() for _ in range(count_participants)]
    for index, value in enumerate(entries):
        entries[index] = (-int(value[1]), int(value[2]), value[0])
    for item in quicksort(entries):
        print(item[2])
