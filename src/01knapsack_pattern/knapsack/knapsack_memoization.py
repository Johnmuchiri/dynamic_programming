def _knapsack(profits, weights, capacity, mem, current_index):

    if capacity <= 0 or current_index >= len(profits):
        return 0

    if mem[current_index][capacity] != -1:
        return mem[current_index][capacity]

    profit1 = 0
    if weights[current_index] <= capacity:

        profit1 = profits[current_index] + _knapsack(profits, weights, capacity - weights[current_index],
                                                     mem, current_index + 1)

    profit2 = _knapsack(profits, weights, capacity, mem, current_index + 1)

    mem[current_index][capacity] = max(profit1, profit2)

    return mem[current_index][capacity]


def knapsack(profits, weights, capacity):
    mem = [[-1 for _ in range(capacity+1)] for _ in range(len(weights))]
    return _knapsack(profits, weights, capacity, mem, 0)


profits = [1, 6, 10, 16]
weights = [1, 2, 3, 5]
capacity = 7
print(knapsack(profits, weights,capacity))



"""
Time complexity 0(N*C)
space complexity 0(N*C+ N) =>0(N*C) 

"""
