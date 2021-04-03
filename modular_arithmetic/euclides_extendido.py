#!/usr/bin/env python3

from coc_resto import coc_resto

def euclides_extendido(a, b):
    """ Retorna el máximo común divisor, alfa y beta haciendo uso del algoritmo
    extendido de Euclides de forma recursiva. """
    if b > a:
        euclides_extendido(b, a)
    if b == 0:
        alfa = 1
        beta = 0
        mcd = a
        return (mcd, alfa, beta)
    else:
        (cociente, resto) = coc_resto(a, b)
        (mcd_resto, alfa_resto, beta_resto) = euclides_extendido(b, resto)
        alfa = beta_resto
        beta = alfa_resto - beta_resto * cociente
        mcd = mcd_resto
        return (mcd, alfa, beta)


if __name__ == '__main__':
    import sys
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    (mcd, alfa, beta) = euclides_extendido(a, b)
    print('mcd: {}, alfa: {}, beta: {}'.format(mcd, alfa, beta))
        
