#!/usr/bin/env python3

from euclides_extendido import euclides_extendido
from coc_resto import coc_resto

def div_cero_invertible(n, x):
    """" Retorna una tupla, indicando si x mod n es un divisor de cero, o  invertible y el inverso
    el caso de que sea invertile (divisor, invertible, inverso). """
    
    (mcd, alfa, _) = euclides_extendido(x, n)   # Calcula el máximo común divisor y el valor de alfa
    if mcd != 1:
        divisor = True
        invertible = False
        inverso = 'No existe'
    elif mcd == 1:
        divisor = False
        invertible = True
        (_, inverso) = coc_resto(alfa, n)
    return (divisor, invertible, inverso)

if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    x = int(sys.argv[2])
    (divisor, invertible, inverso) = div_cero_invertible(n, x)
    print('divisor: {}, invertible: {}, inverso: {}'.format(divisor, invertible, inverso))
    
    
