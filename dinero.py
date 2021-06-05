#!/usr/bin/env python3

class Dinero(object):
    """La clase representa un monto de dinero en una
    moneda específica"""

    def __init__(self, cantidad, moneda='$'):
        """ Inicializa los atributos cantidad y moneda"""
        self.cantidad = cantidad
        self.moneda = moneda

    def suma(self, nueva_cantidad):
        self.cantidad = self.cantidad + nueva_cantidad

    def resta(self, nueva_cantidad):
        self.cantidad = self.cantidad - nueva_cantidad

    def multiplicar(self, veces):
        self.cantidad = self.cantidad * veces

    def dividir(self, veces):
        self.cantidad = self.cantidad / veces

    def __str__(self):
        return "{} {}".format(self.moneda, self.cantidad)


if __name__ == "__main__":
    dinero = Dinero(5)
    print(dinero)
    dinero.suma(1)
    print(dinero)
    dinero.resta(5)
    print(dinero)
    dinero.multiplicar(6)
    print(dinero)
    dinero.dividir(5)
    print(dinero)
