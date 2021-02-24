#!/usr/bin/env python3

n_archivo = input("Escriba el nombre del archivo: ")
substring = input("Escriba la subcadena a encontrar: ")

try:
    ma = open(n_archivo)
except:
    print("No se puede encontrar el archivo: ", n_archivo)
    exit()


contador = 0
for linea in ma:
    palabras = linea.split()
    for palabra in palabras:
        if palabra.find(substring) == -1:
            continue
        print(palabra)
        contador += 1

if contador == 0:
    print("Ninguna palabra cumple con el criterio de búsqueda: {}".format(substring))
else:
    print("Hay {} palabras que contiene {}".format(contador, substring))
