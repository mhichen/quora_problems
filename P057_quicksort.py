#!/usr/bin/python3

def partition(arr, lo, hi):

    pivot = arr[hi]

    pind = lo

    for i in range(lo, hi):

        if arr[i] < pivot:

            arr[i], arr[pind] = arr[pind], arr[i]
            pind += 1

    arr[hi], arr[pind] = arr[pind], arr[hi]

    return pind

def quicksort(arr, lo, hi):

    if (lo >= hi):
        return

    pivot = partition(arr, lo, hi)

    quicksort(arr, lo, pivot - 1)

    quicksort(arr, pivot + 1, hi)
    

if __name__ == "__main__":

    A = [9, -3, 5, 2, 6, 8, -6, 1, 3]

    n = len(A)

    print(A)

    quicksort(A, 0, n - 1)

    print(A)
