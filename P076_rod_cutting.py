#!/usr/bin/python3


# Given price per length and target rod length
# return maximum profit
def rod_cut(price, target):

    n = len(price)

    # Use an array to keep track of max value per length
    # Base case is zero length, zero profit
    T = [0] * (target + 1)

    # Iterate over target length
    for i in range(1, target + 1):

        # Iterate over prices/segments
        for j in range(1, i + 1):

            T[i] = max(T[i],
                       T[i - j] + price[j - 1])

    return T[target]

if __name__ == "__main__":

    price = [1, 5, 8, 9, 10, 17, 17, 20]
    target = 4

    # Expect 10
    print(rod_cut(price, target))
