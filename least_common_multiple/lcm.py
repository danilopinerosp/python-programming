#!/usr/bin/env python3

def calculate_lcm(a, b):
    """ Returns the least common multiple of a and b"""
    
    if a < b:
        a, b = b, a

    found = False
    counter = 1

    while not found:
        if (a * counter) % b == 0:
            result = a * counter
            found = True
        counter += 1

    return result

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    lcm = calculate_lcm(a, b)
    print(lcm)
