#!/usr/bin/env python3

def es_primo(n):
    resultado = True
    if n <= 1:
        resultado = False
    elif n % 2 == 0 and n != 2:
        resultado = False
    else:
        contador = 3
        while contador < (n + 1) // 2 and resultado:
            if n % contador == 0:
                resultado = False
            contador += 2
    return resultado

def factores_primos(n):
    pass
