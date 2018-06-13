#!/usr/bin/python3


# given value and weight arrays, figure out maximum value
# given a target weight
# Returns: maximum value
def knapsack(value, weight, target):

    n = len(value)

    # Use a matrix T to keep track of maximum value
    # given
    # (n + 1) x (target + 1)
    T = [[None] * (target + 1) for i in range(n + 1)]

    # First row is if no elements to add, so all zeros
    for j in range(target + 1):
        T[0][j] = 0

    # iterate over items
    for i in range(1, n + 1):

        # iterate over target weight/capacity
        for j in range(0, target + 1):

            # include vs exclude

            # exclude if exceeds weight limit
            if (weight[i - 1] > j):
                T[i][j] = T[i - 1][j]
            # otherwise, add
            else:
                T[i][j] = max(T[i - 1][j],
                              T[i - 1][j - weight[i - 1]] + value[i - 1])

    return T[n][target]
            


if __name__ == "__main__":

    value = [20, 5, 10, 40, 15, 25]
    weight = [1, 2, 3, 8, 7, 4]
    target = 10

    # Expect 60
    print(knapsack(value, weight, target))
