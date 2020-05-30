def target_sum(arr, sum):
    n = len(arr)
    if sum == 0:
        return True
    dp = [[False for i in range(sum + 1)] for j in range(n+1)]
    ### We can acheive wight zero by picking any item
    """
    
    Table example below
    
    0 1 2 3 4 5
   0 T
   1 T
   2 T
   4 T
    """
    for i in range(n+1):
        dp[i][0] = True
    """
    with item 0 we can only make weight where the value of item at 0 is equal to the weight
    in this case the true value is alredy filled up
        0 1 2 3 4 5
   0    T F F F F F
   1 
   2 
   4 
    """

    for j in range(1, sum + 1):
        dp[0][j] = False


    ##Other cases
    for i in range(1, n+1):
        for j in range(1, sum + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]

            elif arr[i] <= sum:
                dp[i][j] = dp[i - 1][sum - arr[i]] or dp[i - 1][j]

    """the value of the last cell should be the return value
     and if true, it means there is a subset that sums to our given sum
     """
    return dp[n - 1][sum]

arr = [3, 34, 4, 12, 5, 2]
sum = 9
print(target_sum(arr, sum))

