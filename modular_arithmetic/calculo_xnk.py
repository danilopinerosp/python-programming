#!/usr/bin/env python3

from coc_resto import coc_resto

def calculo_xnk(x, n, k):
    """ Retorna el valor x^k mod n calculado de forma recursiva."""

    if k == 0:  # Caso base
        return 1
    elif k == 1:
        (_, xnk) = coc_resto(x, n)
        return xnk
    else:
        new_k = k // 2
        a = calculo_xnk(x, n, new_k)
        b = calculo_xnk(x, n, k -  new_k)
        (_, xnk) = coc_resto(a * b, n)
        return xnk

if __name__ == '__main__':
    import sys
    x = int(sys.argv[1])
    n = int(sys.argv[2])
    k = int(sys.argv[3])
    xnk = calculo_xnk(x, n, k)
    print('x^k mod n: {}'.format(x, n, k))
