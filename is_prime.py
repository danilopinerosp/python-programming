#!/usr/bin/env python3

def is_prime(n):
    if n < 2:
        return False
    k = 2
    while k <= n / 2:
        if n % k == 0:
            return False
        k += 1
    return True        


if __name__ == "__main__":
    n = int(input('>> '))
    print(is_prime(n))
