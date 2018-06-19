#!/usr/bin/python3

import numpy as np

# Given an unlimited supply of coins, find min number
# of coins to get change
def get_change(denom, target):

    # Use an array to get min number of coins needed
    # to make change
    # will have size target
    # T[0]: min coins needed for change of 0 (0)
    # T[1]: min coins needed for change of 1 (1)
    # ...
    # T[5]: min coins needed for change of 3 (1)
    T = [np.inf] * (target + 1)

    T[0] = 0

    for t in range(1, target + 1):

        for d in denom:

            # if can make change
            if (t - d) >= 0:
                T[t] = min(T[t], T[t - d] + 1)

    return T[target]

if __name__ == "__main__":


    denominations = [1, 3, 5, 7]

    print(get_change(denominations, 15))

    denominations = [1, 2, 3, 4]

    print(get_change(denominations, 18))
        
