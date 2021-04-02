#!/usr/bin/env python3

from coc_resto import coc_resto

def mcd_euclides(a, b):
    """ Retorna el máximo común divisor calculado usando el algoritmo de euclides de forma recursiva. """
    if b > a:
        mcd_euclides(b, a)
    if b == 0:
        return a
    else:
        (_, resto) = coc_resto(a, b)
        return mcd_euclides(b, resto)

if __name__ == '__main__':
    import sys
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    mcd = mcd_euclides(a, b)
    print('El máximo común divisor entre {} y {} es {}'.format(a, b, mcd))
