#!/usr/bin/env python3

def last_digit_fib(n):
    """ Returns the last digit of the fibonacci of n, using a divide and conquer 
    algorithm"""

    if n <= 0:
        return 0

    i = n - 1

    aux_one = 0
    aux_two = 1
    (a, b) = (aux_two, aux_one)
    (c, d) = (aux_one, aux_two)

    while i > 0:
        if i % 2 != 0:
            aux_one = (d*b + c*a) % 10
            aux_two = (d*(b + a) + c * b) % 10
            (a, b) = (aux_one, aux_two)

        aux_one = (c**2 + d**2)
        aux_two = (d * (2 * c + d))
        (c, d) = (aux_one, aux_two)
        i = i // 2

    return (a + b) % 10


def calculate_last_digit_sum(n):
    """ Returns de last  digit of of sum first n digits of fibonacci numbers"""
    return last_digit_fib(n + 2) - 1


if __name__ == "__main__":
    n = int(input())
    result = fib(n)
#    result = calculate_last_digit_sum(n)
    print(result)
