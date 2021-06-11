#!/usr/bin/env python3

from fibonacci import fib_list

def pisano_period(m):
    """ Returns the lenght of the pisado period"""
    
    if m == 1:
        return 1

    previous, current = 0, 1

    for i in range(1, m * m):
        previous, current = current, (previous + current) % m
        if previous + current == 1:
            return i + 1

def fibonacci_module(n, m):
    """ Returns the fibonacci number n module m"""
    pisano = pisano_period(m)
    n = n % pisano

    result = fib_list(n) % m
    return result
