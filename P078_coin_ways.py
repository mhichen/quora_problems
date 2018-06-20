#!/usr/bin/python3


def num_ways(denom, target):

    n = len(denom)
    
    # use matrix to keep track of number of ways
    # to get change j with 1 - i coins
    # dimensions of (n + 1) x (target + 1)
    T = [ [None] * (target + 1) for i in range(n + 1) ]


    # first row corresponds to 0 coins
    for j in range(target + 1):
        T[0][j] = 0

    # first column corresponds to exactly one way to return change
    # i.e. zero coins
    for i in range(n + 1):
        T[i][0] = 1
    

    for i in range(1, n + 1):

        for j in range(1, target + 1):

            # exclude since coin addition exceeds change amount
            if j - denom[i - 1] < 0:
                T[i][j] = T[i - 1][j]
                
            # include
            else:
                T[i][j] = T[i][ j - denom[i - 1] ] + T[i - 1][j]

    return T[n][target]
    


if __name__ == "__main__":

    
    denominations = [1, 3, 5, 7]

    # expect 6
    print(num_ways(denominations, 8))
