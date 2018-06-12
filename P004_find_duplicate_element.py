#!/usr/bin/python3

# Find duplicate element in limited range
# Use XOR -- First take XOR of all elements in the array
# Then take XOR of elements from 0 - (len(arr) - 1)
def find_duplicate_element_v1(arr):

    result = 0

    for a in arr:

        result ^= a

    # skip 0
    for i in range(1, len(arr)):

        result ^= i

    return result

# Straight up take the difference between
# sum(arr) and expected sum
def find_duplicate_element_v2(arr):

    arr_sum = sum(arr)
    
    exp_sum = (len(arr) * (len(arr) - 1))//2

    return (arr_sum - exp_sum)
    
if __name__ == "__main__":

    A = [1, 2, 3, 4, 4]

    # expect 4
    print(find_duplicate_element_v1(A))
    print(find_duplicate_element_v2(A))
    print()

    B = [1, 2, 3, 4, 2]

    # expect 2
    print(find_duplicate_element_v1(B))
    print(find_duplicate_element_v2(B))
