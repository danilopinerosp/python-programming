#!/usr/bin/env python3

def print_board(figure, word, guess):
    """ Print the board for the game"""
    print(figure)
    print("    " + guess)
    print("+" * 10)

def result(word, guess):
    if word == guess:
        print("Congratulations, you won!")
    else:
        print("You lost")

    
def c_word(words):
    """ Return a word chooses randomly from the list words"""
    return random.choice(words)

import random

figuras_ahorcado = ["""
  +---+
      |
      |
      |
      |
  ---------
  ---------""", """
  +---+
      |
  o   |   
      |
      |
  ---------
  ---------""", """
  +---+
      |
  o   |   
  |   |   
      |
  ---------
  ---------""", """
  +---+
      |
  o   |   
 /|   |  
      |
  ---------
  ---------""", """
  +---+
      |
  o   |  
 /|\  |  
      |
  ---------
  ---------""", """
  +---+
      |
  o   |   
 /|\  |  
   \  |  
  ---------
  ---------""", """
  +---+
      |
  0   |   
 /|\  |
 / \  |  
  ---------
  ---------""", """
  +---+
  |   |
  ô   |
 /|\  |
 / \  |
  ---------
  ---------"""]

palabras = ['armario', 'silla', 'mesa', 'cuerpo', 'brazos', 'cabeza']
palabra = c_word(palabras).upper()
adivinar = "_" * len(palabra)
contador = 0
figura = ""



while figura != figuras_ahorcado[len(figuras_ahorcado) - 1] and adivinar != palabra:
    print_board(figura, palabra, adivinar)
    letra = input('> ')
    letra = letra.upper()
    if letra  not in palabra.upper():
        figura = figuras_ahorcado[contador]
        contador += 1
    else:
        for i in range(len(palabra)):
            if letra == palabra[i]:
                adivinar = adivinar[:i] + letra + adivinar[i + 1:]


result(palabra, adivinar)

if __name__ == "__main__":
    pass
