def can_partition(nums):
    s = sum(nums)
    if s % 2 != 0:
        return False

    s = int(s / 2)
    n = len(nums)
    dp = [[False for i in range(s + 1)] for y in range(n)]
    """populate the column where sum is 0 since we can gave 0 without including any item"""
    for i in range(0, n):
        dp[i][0] = True

    """with one number we can only acheive the sum if the number and the sum are the same"""
    for j in range(1, s + 1):
        if j == nums[0]:
            dp[0][j] = True
    """processing all other cases sum"""

    for i in range(1, n):
        for j in range(1, s+1):
            """if the previous computed value dp[i-1][j] is true  then dp[i][j] should be true"""
            if dp[i-1][j]:
                dp[i][j] =dp[i-1][j]
            if j>=nums[i]:
                dp[i][j] =dp[i-1][j-nums[i]]

    return dp[n-1][s]

nums =[1, 2, 3,4]
print(can_partition(nums))


"""Time complexity 0(N*C) where N is the number of items in the array and s is the total sum of all numbers"""
