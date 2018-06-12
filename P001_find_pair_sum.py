#!/usr/bin/python3

# Given array and a sum, find pair resulting in the sum
# Use hash table
def find_pair_sum(arr, target):

    my_dict = {}

    for i in range(0, len(arr)):

        if arr[i] not in my_dict:
            my_dict[arr[i]] = i

        if (target - arr[i]) in my_dict:
            return (my_dict[target - arr[i]], i)
    

if __name__ == "__main__":


    A = [4, 2, 3, 0, 5, 9, 8]

    target = 9

    print(find_pair_sum(A, target))
