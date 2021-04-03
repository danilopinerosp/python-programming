#!/usr/bin/env python3

from div_cero_invertible import div_cero_invertible

def vectores_ceros_inversos(n):
    """ Retorna una tupla con tres listas donde se especifican los divisore de cero, los invertibles y los inversos del número narual n."""
    divisores_ceros = list()
    invertibles = list()
    inversos = list()

    for i in range(1, n):
        (divisor_cero, invertible, inverso) = div_cero_invertible(n, i)
        if divisor_cero:
            divisores_ceros.append(i)
        elif invertible:
            invertibles.append(i)
            inversos.append(inverso)

    return (divisores_ceros, invertibles, inversos)

if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    resultado = vectores_ceros_inversos(n)
    print('Divisores de cero: {}'.format(resultado[0]))
    print('Invertibles: {}'.format(resultado[1]))
    print('Inversos: {}'.format(resultado[2]))
    
