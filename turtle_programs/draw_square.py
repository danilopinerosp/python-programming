#!/usr/bin/env python3

import turtle

def draw_square(pen, n):
    """ Pen draws a square with sides of length n"""
    for i in range(4):
        pen.forward(n)
        pen.left(90) # Pen turns left 90 degrees

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("My first square")

    square = turtle.Turtle()
    draw_square(square, 70)

    screen.mainloop()
