# https://contest.yandex.ru/contest/23390/run-report/54700743/


def find_distance_zero(street_lenght, lands):
    EMPTY_LAND = "0"

    distance_zero = [0] * street_lenght
    if lands[0] != EMPTY_LAND:
        distance_zero[0] = float('inf')
    for i, land in enumerate(lands[1::], start=1):
        distance_zero[i] = distance_zero[i - 1] + 1
        if land == EMPTY_LAND:
            distance_zero[i] = 0
    if lands[-1] == EMPTY_LAND:
        distance_zero[-1] = 0
    distance_zero = distance_zero[::-1]
    lands = lands[::-1]
    for j, land in enumerate(lands[1::], start=1):
        distance_zero[j] = min(distance_zero[j], distance_zero[j - 1] + 1)
        if land == 0:
            distance_zero[j] = 0

    return distance_zero[::-1]


if __name__ == '__main__':
    street_lenght = int(input())
    lands = input().split()
    print(*find_distance_zero(street_lenght, lands))
