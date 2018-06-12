#!/usr/bin/python3

# Sort binary array in linear time
def sort_binary_array(arr):

    pivot = 1
    
    # Use a read/write index
    # Swap the two every time the read index encounters a value less than pivot
    w = 0

    for r in range(0, len(arr)):

        if arr[r] < pivot:

            arr[r], arr[w] = arr[w], arr[r]

            w += 1


if __name__ == "__main__":

    A = [1, 0, 1, 0, 1, 0, 0, 1]

    print(A)
    sort_binary_array(A)
    print(A)
