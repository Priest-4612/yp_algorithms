# https://contest.yandex.ru/contest/24735/run-report/55752309/
def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_element = nums[mid]
        if mid_element == target:
            return mid
        left_element = nums[left]
        if left_element == target:
            return left
        if left_element < mid_element or left_element == mid_element:
            if left_element < target < mid_element:
                right = mid - 1
            else:
                left = mid + 1
        else:
            right_element = nums[right]
            if target == right_element:
                return right
            if mid_element < target < right_element:
                left = mid + 1
            else:
                right = mid - 1
    return -1
