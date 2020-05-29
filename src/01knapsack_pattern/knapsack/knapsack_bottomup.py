def knapsack(profits, weights, capacity):
    if len(profits) != len(weights) or capacity <= 0 or len(profits) <= 0:
        return 0
    dp = [0 for _ in range(capacity + 1) for _ in range(len(weights))]
    # when the capacity is 0 the profits shoulw be zero too
    for i in range(0, len(profits)):
        dp[i][0] = 0
    ##when the weight is zero then the capacity is zero
    for i in range(capacity + 1):
        if weights[0] <= capacity:
            dp[0][capacity] = profits[0]

    for i in range(len(weights)):
        for j in range(capacity + 1):
            profit1, profit2 = 0, 0
            # include current weight
            if weights[i] <= capacity:
                profit1 = profits[i] + dp[i - 1][capacity - weights[i]]
            #exclude current weight
            profit2 = dp[i - 1][capacity - weights[i]]

            dp[i][j] = max(profit2, profit1)
    return dp[len(weights) - 1][capacity]


print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))