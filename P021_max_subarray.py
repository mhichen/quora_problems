#!/usr/bin/python3


# Find subarray with maximum sum
def max_subarray(arr):

    # keep track of max_ending_here and max_so_far
    # the idea is to check if the addition of the current
    # element will add or subtract from the sum
    max_ending_here = arr[0]
    max_so_far = arr[0]

    for a in arr:
        max_ending_here = max(max_ending_here + a, a)
        max_so_far = max(max_ending_here, max_so_far)

    return max_so_far

if __name__ == "__main__":

    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    print(max_subarray(A))
