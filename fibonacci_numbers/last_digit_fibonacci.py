#!/usr/bin/env python3

def last_digit_fibonacci(n):
    """ Returns the las digit of the fibonacci number of n.

    Parameters:
    -----------
    n -> int : Positive integer number

    Returns:
    --------
    int : Positive integer number of just one digit
    """
    
    fib_digits = [0, 1]
    if n <= 1: # Basecase
        f_i = fib_digits[n]
    
    for i in range(2, n + 1):
        f_i = (fib_digits[0] + fib_digits[1]) % 10
        fib_digits[0] = fib_digits[1]
        fib_digits[1] = f_i

    return f_i

if __name__ == "__main__":
    n = int(input())
    print(last_digit_fibonacci(n))
