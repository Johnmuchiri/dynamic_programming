def subset_sum(nums, sum):
    def _subset_sum(nums, sum, dp, current_index):
        print(dp)
        n = len(nums)
        if sum == 0: return 1
        if n==0 or current_index >= n:
            return 0
        if dp[current_index][sum] == -1:
            if nums[current_index] <= sum:
                if _subset_sum(nums, dp, sum - nums[current_index], current_index + 1) == 1:
                    dp[current_index][sum] = 1
                    return 1
            dp[current_index][sum] = _subset_sum(nums, dp, sum, current_index + 1)
        return  dp[current_index][sum]

    dp = [[-1 for i in range(sum+1)] for j in range(len(nums))]
    return _subset_sum(nums, sum, dp, 0)


print(subset_sum([1, 2, 7, 1, 5], 10))
