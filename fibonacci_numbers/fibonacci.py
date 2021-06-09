#!/usr/bin/env python3

def fib_recurs(n):
    """ Returns the fibonacci number of n calculated recursively.
    
    Parameters:
    ----------
    n -> int : Positive integer number

    Return:
    ------
    int : Fibonacci number of n
    """
    if n <= 1: # Basecases
        return n
    else: # Recursive cases
        return fib_recurs(n - 1) + fib_recurs(n - 2)


def fib_list(n):
    """ Returns the fibonacci number of n calculated using a list

    Parameters:
    ----------
    n -> int : Positive integer number

    Return:
    ------
    int : Fibonacci number of n calculated using lists
    """
    f = [0, 1]
    if n <= 1: # Basecase
        return f[n]
    else:
        # Iterate from 2 to n
        for i in range(2, n + 1):
            f = f + [f[i - 1] + f[i - 2]]
    return  f[n]
