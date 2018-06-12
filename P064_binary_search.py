#!/usr/bin/python3

def binary_search(arr, target):

    lo = 0
    hi = len(arr) - 1

    while (lo <= hi):

        mid = lo + (hi - lo)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1

    return None


def binary_search_recursive(arr, lo, hi, target):

    # base case of if lo > hi
    if (lo > hi):
        return None

    mid = lo + (hi - lo)//2

    if (arr[mid] == target):
        return mid

    elif arr[mid] > target:
        return binary_search_recursive(arr, lo, mid - 1, target)

    else:
        return binary_search_recursive(arr, mid + 1, hi, target)

if __name__ == "__main__":

    A = [2, 3, 5, 7, 9]
    target = 7
    
    print(binary_search(A, target))


    print(binary_search_recursive(A, 0, len(A) - 1, target))
