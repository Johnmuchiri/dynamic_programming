"""

Find the number of ways you can make a change  of the given amount using the coins given
Given: Coins of different denominations and the total change value

"""

import sys

from typing import List


def coin_change_1(coins: List, change: int) -> int:
    cache = [[0 for _ in range(change)] for _ in range(len(coins))]
    max_val = -sys.maxsize - 1

    for i in range(len(coins)):
        cache[i][0] = 1

    for i in range(len(coins)):

        for j in range(change):
            if coins[i] > j:
                cache[i][j] = cache[i - 1][j]
            else:
                cache[i][j] = (cache[i - 1][j] + cache[i][j - coins[i]])

    print(cache)


coins = [2, 3, 5, 10]
w = 15

arr = [1, 2, 3]
m = len(arr)
n = 4

coin_change_1(arr, n)
