#!/usr/bin/env python3

import turtle

def draw_clock(pen, size):
    """ Draw the face of a clock"""
    pen.shape("turtle")
    pen.stamp()
    for _ in range(12):
        pen.penup()
        pen.forward(size - 30)
        pen.pendown()
        pen.forward(10)
        pen.penup()
        pen.forward(20)
        pen.stamp()
        pen.forward(-size)
        pen.right(360/12)

if __name__ == "__main__":

    window = turtle.Screen()
    pen = turtle.Turtle()
    draw_clock(pen, 200)
    window.mainloop()
