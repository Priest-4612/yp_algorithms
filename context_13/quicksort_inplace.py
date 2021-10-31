# https://contest.yandex.ru/contest/24735/run-report/55747036/
import random


def quicksort(array):

    def quicksort_inplace(start, end):
        if start >= end:
            return
        increase, decline = start, end
        pivot = array[random.randint(start, end)]
        while increase <= decline:
            while array[increase] < pivot:
                increase += 1
            while pivot < array[decline]:
                decline -= 1
            if increase <= decline:
                array[increase], array[decline] = array[decline], \
                                                  array[increase]
                increase, decline = increase + 1, decline - 1
        quicksort_inplace(start, decline)
        quicksort_inplace(increase, end)

    quicksort_inplace(0, len(array) - 1)
    return array


if __name__ == '__main__':
    print(
        *(
            login
            for _, _, login
            in quicksort(
                [
                    (lambda login, count_problem, amount_fine:
                        (-int(count_problem), int(amount_fine), login))
                    (*input().split())
                    for _ in range(int(input()))
                ]
            )
        ),
        sep='\n'
    )
