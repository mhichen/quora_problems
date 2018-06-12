#!/usr/bin/python3

# Given an array with two elements swapped, sort
# the array with one swap
def sort_with_one_swap(arr):

    i = -1
    j = -1

    for k in range(1, len(arr)):

        if arr[k - 1] > arr[k]:

            if i == -1:
                i = k - 1

            else:
                j = k

    arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":

    A = [3, 8, 6, 7, 5, 9]

    print(A)
    sort_with_one_swap(A)
    print(A)
