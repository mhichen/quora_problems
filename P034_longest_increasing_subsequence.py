#!/usr/bin/python3

import numpy as np

# Returns length of longest increasing subsequence
def longest_increasing_subsequence(arr):

    n = len(arr)
    
    # Use array to keep track of longest increasing subsequence ending
    # at position i
    L = [0] * n

    L[0] = 1

    for i in range(1, n):

        for j in range(0, i):
            
            # include if current element is larger than element value between 0 and i - 1
            if arr[i] > arr[j] and (L[j] + 1 > L[i]):
                L[i] = L[j] + 1

    return max(L)


# Recursive solution
def LIS(arr, prev, curr_ind, n):

    # base case if curr_ind >= n, then return
    if curr_ind >= n:
        return 0

    # exclude
    excl = LIS(arr, prev, curr_ind + 1, n)

    incl = 0
    
    # include -- only if curr element > prev element
    if (arr[curr_ind] > prev):
        incl = 1 + LIS(arr, arr[curr_ind], curr_ind + 1, n)

    return max(incl, excl)
    

if __name__ == "__main__":

    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

    # Expect 6
    print(longest_increasing_subsequence(A))

    print(LIS(A, -np.inf, 0, len(A)))
