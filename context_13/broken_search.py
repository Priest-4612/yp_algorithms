# https://contest.yandex.ru/contest/24735/run-report/55746578/
def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_element = nums[mid]
        if mid_element == target:
            return mid
        if nums[left] <= mid_element:
            if nums[left] <= target < mid_element:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if mid_element < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
