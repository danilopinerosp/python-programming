#!/usr/bin/env python3

import math

def q_equation(a, b, c):
    """ Return the values of x that the quadratic equation with coefficients a, b, and c is solved."""
    r = (b**2)-(4*a*c) # Save the term that we've got to take the square root from.
    if r < 0:
        r = -1 * r
        r_sqrt = math.sqrt(r) * complex("j")
    else:
        r_sqrt = math.sqrt(r)
    x1 = (-b + r_sqrt)/(2*a)
    x2 = (-b - r_sqrt)/(2*a)
    return (x1, x2)

if __name__ == "__main__":
    try:
        a = float(input("Ingrese a: "))
        b = float(input("Ingrese b: "))
        c = float(input("Ingrese c: "))
        x1, x2 = q_equation(a, b, c)
        print("x1: {}, x2: {}".format(x1, x2))
    except:
        print("Only numerical values are allowed")        
