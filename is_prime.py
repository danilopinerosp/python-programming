#!/usr/bin/env python3

def is_prime(n):
    """ Returns True is n is prime, False otherwise"""
    
    result = True
    if n < 2:
        result = False
    k = 2
    while k <= n / 2 and result:
        if n % k == 0:
            result = False
        k += 1
    return result


if __name__ == "__main__":
    n = int(input('>> '))
    print(is_prime(n))
