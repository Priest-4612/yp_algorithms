def quicksort_inplace(list, start=0, end=None):
    pass


if __name__ == '__main__':
    count_participants = int(input())
    entries = [input().split(' ') for _ in range(count_participants)]

    print(
        f'Количество участников: {count_participants}'
        f'\nСписки участников {entries}'
    )
