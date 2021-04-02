#!/usr/bin/env python

def coc_resto(a, b):
    cociente = a // b
    resto = a % b
    return (cociente, resto)


if __name__ == '__main__':
    import sys
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    (cociente, resto) = coc_resto(a, b)
    print('{} / {} tiene cociente: {}, resto: {}'.format(a, b, cociente, resto))
