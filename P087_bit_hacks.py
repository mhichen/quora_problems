#!/usr/bin/python3

# Check if number is odd
def is_odd(n):

    return (n & 1)

# Check if 2 integers have opposite signs
def opposite_signs(a, b):

    return True if (a ^ b) < 0 else False

def add_1(a):

    return -~a

def swap(a, b):

    a = a ^ b
    b = a ^ b
    a = a ^ b

    return a, b


if __name__ == "__main__":

    print(is_odd(10))
    print(is_odd(11))
    print()
    
    print(opposite_signs(1, 2))
    print(opposite_signs(1, -2))
    print()

    print(add_1(2))
    print(add_1(-3))
    print()
    
    a = 1
    b = 5
    print("a = ", a)
    print("b = ", b)
    a, b = swap(a, b)
    print("a = ", a)
    print("b = ", b)
    print()
    
    
