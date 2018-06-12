#!/usr/bin/python3

import numpy as np


# use a visited array to check if array is composed of consecutive integers
def is_consecutive(arr, i, j, min_val, max_val):

    # difference between max and min element should be equal to j - 1
    if (max_val - min_val) != (j - i):
        return False

    # a visited array
    visited = np.zeros(j - i + 1)

    for val in arr[i:j]:

        # if element has been seen, return False
        if (visited[val - min_val]):
            return False

        visited[val - min_val] = 1

    return True

def largest_consecutive_subarray(arr):

    # keep track of longest length and indices of start and end of array
    length = 1
    start = 0
    end = 0

    # Difference between max and min element should be equal to
    # the length of the subarray minus one
    for i in range(0, len(arr) - 1):

        min_val = arr[i]
        max_val = arr[i]

        for j in range(i + 1, len(arr)):

            if arr[j] > max_val:
                max_val = arr[j]

            if arr[j] < min_val:
                min_val = arr[j]

            if (is_consecutive(arr, i, j, min_val, max_val)):

                if (length < (max_val - min_val + 1)):
                    length = max_val - min_val + 1
                    start = i
                    end = j

    print(start, end)


if __name__ == "__main__":

    A = [2, 0, 2, 1, 4, 3, 1, 0]

    # Expect [0, 2, 1, 4, 3]
    # Return indices [1, 5]
    largest_consecutive_subarray(A)
