#!/usr/bin/python3


# Given an array, find the majority element
def find_majority_element(arr):

    # keep track of most recent element
    elem = 0
    
    # keep count
    count = 0

    for i in range(1, len(arr)):

        # if count is zero, then save curr element and increment count
        if count == 0:
            elem = arr[i]
            count = 1

        elif elem == arr[i]:
            count += 1

        else:
            count -= 1

    return elem




if __name__ == "__main__":

    A = [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]

    print(find_majority_element(A))

