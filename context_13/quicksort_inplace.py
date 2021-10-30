# https://contest.yandex.ru/contest/24735/run-report/55687014/
import random


def to_participant(login, count_problem, amount_fine):
    return (-int(count_problem), int(amount_fine), login)


def subpart_partition(array, start, end, paviot_index):
    if not (start <= paviot_index <= end):
        raise ValueError('paviot_index должна быть между start и end')
    array[start], array[paviot_index] = array[paviot_index], array[start]
    paviot = array[start]
    partition = start + 1
    curren = start + 1
    while curren <= end:
        if array[curren] <= paviot:
            array[curren], array[partition] = array[partition], array[curren]
            partition += 1
        curren += 1

    array[start], array[partition - 1] = array[partition - 1], array[start]
    return partition - 1


def quicksort_inplace(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if end - start < 1:
        return

    paviot_index = random.randint(start, end)
    partition = subpart_partition(array, start, end, paviot_index)
    quicksort_inplace(array, start, partition - 1)
    quicksort_inplace(array, partition + 1, end)


if __name__ == '__main__':
    count_participants = int(input())
    entries = [to_participant(*input().split())
               for _ in range(count_participants)]
    quicksort_inplace(entries)
    result = (login for _, _, login in entries)
    print(*result, sep='\n')
