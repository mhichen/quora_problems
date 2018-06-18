#!/usr/bin/python3

# Longest Palindromic Subsequence -- recursive
def LPS(tstr, lo, hi):

    # base case: lo exceeds hi
    if (lo > hi):
        return 0

    # base case: 1 char is a valid palindrome
    if (lo == hi):
        return 1

    # Case (1) -- lo and hi characters match
    # increment lo, decrement hi, add 2
    if (tstr[lo] == tstr[hi]):
        return LPS(tstr, lo + 1, hi - 1) + 2

    # Case(2) -- take max between incrementing lo
    # and decrementing hi
    else:
        return max( LPS(tstr, lo + 1, hi),
                    LPS(tstr, lo, hi - 1) )
                    

# Longest Palindromic Subsequence -- DP
def LPS_DP(tstr):

    n = len(tstr)

    if (n == 0):
        return 0
    
    # Use a matrix to keep track of max length
    # dimensions of (n x n)
    # T[i][j] represents longest palidronic subsequence
    # length of tstr[i:j+1]
    T = [ [0] * n for i in range(n) ]

    # diagonal is all 1 since 1 char is valid palindrome
    for i in range(n):
        T[i][i] = 1

    # iterate over substring length
    for l in range(2, n + 1):

        # iterate over start index i
        for i in range(0, n - l + 1):

            j = i + l - 1

            if tstr[i] == tstr[j]:
                T[i][j] = T[i + 1][j - 1] + 2
            else:
                T[i][j] = max(T[i + 1][j], T[i][j - 1])

    return T[0][n - 1]
    
    
if __name__ == "__main__":

    tstr = "ABBDCACB"

    # expect 5
    print(LPS(tstr, 0, len(tstr) - 1))

    print(LPS_DP(tstr))
