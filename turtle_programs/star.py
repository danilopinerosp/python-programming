#!/usr/bin/env python3

import turtle

def draw_star(pen, size):
    """ Draw a star of five corners"""
    for _ in range(5):
        if _ == 0:
            pen.right(360/5)
            pen.forward(size)
        else:
            pen.right(360/2.5)
            pen.forward(size)
    pen.right(360/5)

if __name__ == "__main__":

    window = turtle.Screen()
    pen = turtle.Turtle()

    draw_star(pen, 150)

    window.mainloop()
