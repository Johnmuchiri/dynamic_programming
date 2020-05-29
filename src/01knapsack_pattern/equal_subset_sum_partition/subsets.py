"""Print all the subsets of an array"""


def print_set(nums):
    def helper(nums, subset, current_index):
        if current_index == len(nums):
            print(subset)
        else:
            subset[current_index] = None
            helper(nums, subset, current_index + 1)
            subset[current_index] = nums[current_index]
            helper(nums, subset, current_index + 1)

    arr = [0 for i in range(len(nums))]
    helper(nums, arr, 0)


nums = [1, 2]
nums2 = [1, 2, 3, 4]
print_set(nums2)
