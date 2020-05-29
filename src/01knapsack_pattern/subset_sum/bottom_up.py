def subset_sum(arr, sum):
    if sum == 0:
        return 1
    n = len(arr)
    dp = [[False for i in range(sum + 1)] for j in range(n)]

    """when the weight is zero, we can make that sum by picking any number"""
    for i in range(0,n):
        dp[i][0] = True

    """if we pick first item from the array, 
    We can make the sum of j only when arr[i] == j"""

    for j in range(0,sum + 1):
        if arr[i] == j:
            dp[0][j] = True
        else:
            dp[0][j] = False
    """compute the sums for other scenarios"""

    for i in range(1, n):
        for j in range(1, sum + 1):
            if dp[i - 1][j] == 1:
                dp[i][j] = dp[i - 1][j]
            elif arr[i] <= sum:
                dp[i][j] = dp[i - 1][sum - arr[i]]

    return dp[n - 1][sum]


arr = [1, 2,1, 7, 5]
S = 10

"""print(subset_sum(arr, S))"""
print(subset_sum([1, 2, 7, 1, 5], 10))
