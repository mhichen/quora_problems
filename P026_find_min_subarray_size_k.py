#!/usr/bin/python3

def min_sum_subarray(arr, k):

    # use a sliding window to keep track of the current sum
    curr_sum = sum(arr[0:k])
    min_sum = curr_sum
    min_ind = 0

    for i in range(1, len(arr) - k + 1):

        curr_sum = (curr_sum - arr[i - 1] + arr[i + k - 1])

        if curr_sum < min_sum:
            
            min_sum = curr_sum
            min_ind = i

    return min_sum, min_ind, min_ind + k - 1
    

if __name__ == "__main__":
    
    A = [10, 4, 2, 5, 6, 3, 8, 1]

    k = 3
    
    # Output: 11
    print(min_sum_subarray(A, k))
