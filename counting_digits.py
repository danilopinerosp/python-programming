#!/usr/bin/env python3

def counting_digits(number):
    """ Return the number of decimal digits of the positive integer 'number'"""
    count = 0
    while number != 0:
        count = count + 1
        number = number // 10
    return count

if __name__ == "__main__":
    import sys
    try:
        number = int(sys.argv[1])
    except:
        number = 500
    digits = counting_digits(number)
    print(number, "has", digits)
