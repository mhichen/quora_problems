#!/usr/bin/python3

# Given pots of gold where each player
# can pick only from front of back of list,
# find the max amount of gold
def pots_of_gold(pots, lo, hi):

    # base case of 1 element left
    if (lo == hi):
        return pots[lo]

    # if 2 elements left, return max of the two
    if (lo + 1 == hi):
        return max(pots[lo], pots[hi])

    # pick front
    front = pots[lo] + min( pots_of_gold(pots, lo + 2, hi),
                            pots_of_gold(pots, lo + 1, hi - 1) )

    # pick back
    back = pots[hi] + min( pots_of_gold(pots, lo, hi - 2),
                           pots_of_gold(pots, lo + 1, hi - 1) )

    return max(front, back)


if __name__ == "__main__":

    pots = [4, 6, 2, 3]

    print(pots_of_gold(pots, 0, len(pots) - 1))
