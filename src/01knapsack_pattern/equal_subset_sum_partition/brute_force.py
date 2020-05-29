def can_partition(nums):
    s = sum(nums)
    if s % 2 != 0:
        return False
    return _can_partition(nums, s / 2, 0)


def _can_partition(nums, sum, index):
    if sum == 0:
        return True
    n = len(nums)
    if n == 0 or index >= n:
        return False
    if nums[index] <= sum:
        if _can_partition(nums, sum - nums[index], index + 1):
            return True
    return _can_partition(nums, sum, index + 1)


nums =[1, 2, 3, 4]
print(can_partition(nums))

"""
time complexity is 0(2^n)
space complexity of 0(n) for recursion stack
"""