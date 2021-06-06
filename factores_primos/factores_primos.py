#!/usr/bin/env python3

def es_primo(n):
    """Retorna True si n es primo, y False en caso contrario

    Parámetros:
    ----------
    n -> int : Número entero positivo

    Retorna:
    -------
    resultado -> bool : Verdadero si n es primo, y falso en caso contrario
    """
    resultado = True
    if n <= 1: # Cualquier número menor que 1 no es primo
        resultado = False
    elif n % 2 == 0 and n != 2: # Descarta todos los números pares
        resultado = False
    else:
        # Se inicia desde 3 y se evaluan sólo números impares
        contador = 3
        while contador < (n + 1) // 2 and resultado:
            if n % contador == 0:
                resultado = False
            contador += 2
    return resultado

def factores_primos(n):
    """Retorna una lista con los factores primos de n.

    Parámetros:
    ----------
    n -> int : Número entero positivo

    Retorna:
    -------
    resultado -> list : Lista con los factores primos. Será una lista vacía si no hay factores 
                        primos.
    """
    resultado = []
    factor = 2
    while n > 1 and factor <= n:
        while not es_primo(factor) or n % factor != 0:
            factor += 1
        if n % factor == 0:
            resultado = resultado + [factor]
            n /= factor
    return resultado
    
