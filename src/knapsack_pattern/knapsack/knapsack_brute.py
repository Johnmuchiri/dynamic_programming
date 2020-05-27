
def _bruteforce_solution(profits, weights, capacity, current_index):
    ##print(current_index)
    ##boundary cases
    if capacity <= 0 or current_index >= len(profits):
        return 0

    profit = 0

    if weights[current_index] <= capacity:
        ##including the current index weight
        profit = profits[current_index] + _bruteforce_solution(profits, weights, capacity - weights[current_index],
                                                               current_index + 1)
    # excluding the current index weight
    profit1 = _bruteforce_solution(profits, weights, capacity, current_index + 1)

    return max(profit, profit1)


def bruteforce_solution(profits, weights, capacity):
    return _bruteforce_solution(profits, weights, capacity, 0)


profits = [1, 6, 10, 16]
weights = [1, 2, 3, 5]
capacity = 7
print(bruteforce_solution(profits, weights,capacity))

"""
Time complexity 0(2^n)
space complexity 0(n) for recursion stack

"""

