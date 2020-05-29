def can_partition(nums):
    def helper(nums, dp, sum, index):
        if sum == 0:
            return 1
        n = len(nums)
        if n == 0 or index >= n:
            return 0
        if dp[index][sum] == -1:
            if nums[index] <= sum:
                if helper(nums, dp, sum - nums[index], index + 1) == 1:
                    dp[index][sum] = 1
                    return 1
            dp[index][sum] = helper(nums, dp, sum, index + 1)
        return dp[index][sum]
    s= sum(nums)
    dp = [[-1 for _ in range((s/2)+1)] for _ in range(len(nums))]
    print(dp)
    if sum(nums) % 2 != 0:
        return False
    return True if helper(nums, dp, int(sum(nums) / 2), 0) == 1 else False
