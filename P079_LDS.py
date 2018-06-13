#!/usr/bin/python3

# Find length of longest decreasing subsequence
def LDS(arr):

    n = len(arr)
    
    # Use an array to keep track of the longest subsequence
    # up until this point

    T = [0] * n

    # Base case
    T[0] = 1

    # iterate over array
    for i in range(1, n):

        # iterate over from 0 to i
        for j in range(0, i):

            # current element is less than previous elements
            # and longest segment found (T[j]) is longer than
            # current longest segment (T[i]), then just copy
            if arr[j] > arr[i] and T[j] > T[i]:
                T[i] = T[j]

        T[i] += 1
        
    return max(T)


if __name__ == "__main__":

    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

    # Expect 5
    print(LDS(A))
