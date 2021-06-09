#!/usr/bin/env python3

def euclidean_gcd(a, b):
    """Return the greatest common divisor between a and b using euclidean algorithm

    Parameters:
    a -> int : Positive integer number
    b -> int : Positive integer number

    Return:
    -------
    int -> Greatest common divisor between a and b
    """
    if b == 0:
        return a
    elif b > a:
        return  euclidean_gcd(b, a)
    else:
        a_prime = a % b
        return euclidean_gcd(b, a_prime)

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    gcd = euclidean_gcd(a, b)
    print(gcd)
