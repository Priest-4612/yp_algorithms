def binary_search(nums, target, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return target
    elif target < nums[mid]:
        return binary_search(nums, target, left, mid)
    else:
        return binary_search(nums, target, mid + 1, right)


def broken_search(nums, target) -> int:
    array_legth = len(nums)
    left = 0
    right = array_legth - 1
    if array_legth == 1:
        if nums[left] == target:
            return left
        return -1
    while nums[left] >= nums[right]:
        if nums[right] == target:
            return right
        right -= 1
    return binary_search(nums, target, left, right)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    _ = input()
    target = int(input())
    *nums, = map(int, input().split())
    print(broken_search(nums, target))
