#!/usr/bin/python3


# Prints the indices of the beginning and end of sequence
def find_subarray_zero_sum(arr):

    # Keep a hash table with a running sum
    # Use a list as val to handle collisions
    my_dict = {}

    # Add edge case in case subarray starts at beginning of the array
    my_dict[0] = [-1]

    tsum = 0
    
    for ind, val in enumerate(arr):

        tsum += val

        if tsum in my_dict:

            for l in my_dict[tsum]:

                if l != ind:
                    my_dict[tsum].append(ind)
                    print(l + 1, ind)

        else:
            my_dict[tsum] = [ind]

    return
        


if __name__ == "__main__":


    A = [4, 2, -3, -1, 0, 4]

    # 4, 6, 3, 2, 2, 6
    
    # Should return (2, 5)
    find_subarray_zero_sum(A)

    print()

    B = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

    find_subarray_zero_sum(B)
