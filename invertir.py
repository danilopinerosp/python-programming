#!/usr/bin/env python3


def invertir(number):
    '''Invierte el orden de los digitos de un número entero'''
    result = 0
    while number:
        digit = number % 10
        number = (number - digit) // 10
        result = (result * 10) + digit
    return result

if __name__ == "__main__":
    n = int(input(">> "))
    print(invertir(n))
