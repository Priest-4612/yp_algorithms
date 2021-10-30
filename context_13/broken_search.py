# https://contest.yandex.ru/contest/24735/run-report/55703119/
def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_element = nums[mid]
        if mid_element == target:
            return mid
        if nums[left] <= mid_element:
            if target < mid_element and nums[left] <= target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if mid_element < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
