def to_participant(login, count_problem, amount_fine):
    return (-int(count_problem), int(amount_fine), login)


def subpart_partition(array, start, end, paviot_index):
    array[start], array[paviot_index] = array[paviot_index], array[start]
    paviot = array[start]





def quicksort_inplace(array, start=0, end=None):
    pass


if __name__ == '__main__':
    count_participants = int(input())
    entries = [to_participant(*input().split(' '))
               for _ in range(count_participants)]

    print(
        f'Количество участников: {count_participants}'
        f'\nСписки участников {entries}'
    )
