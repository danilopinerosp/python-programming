#!/usr/bin/env python3

import turtle

def setup_screen (title, background='white', screen_size_x=640, screen_size_y=640,
          tracer_size=800):
    print('Set up screen')

    turtle.title(title)
    turtle.setup(screen_size_x, screen_size_y)
    turtle.hideturtle()
    turtle.penup()
    # Batch drawing to the screen for faster rendering
    turtle.tracer(tracer_size)
    turtle.bgcolor(background)  # Set the background colour of the screen


def draw_trunk(size, width, angle, x, y, colour):
    """ Draw a line in the direction of angle, from position (x, y) with a given colour and width.
    Return the position (x, y) after drawing the straight line"""
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
        
    turtle.width(width)
    turtle.left(angle)
    turtle.color(colour)
    turtle.forward(size)
    turtle.right(angle)
    x, y = turtle.position()
    return x, y
    
def fractal_tree(size, width=12, angle=0, x=0, y=-200, colour='brown'):
    x, y = draw_trunk(size, width, angle, x, y, colour)
    delta = 0.5
    if width > delta:
        if width < 1:
            # Change the colour to green to draw the leaves
            colour = 'green'
        # Recursive part of the code to draw the two ways, left and right
        fractal_tree(size / 1.4,  width / 1.3, angle + 30, x, y, colour) # left part
        fractal_tree(size / 1.4,  width / 1.3, angle - 30, x, y, colour) # right part
        
        
    
setup_screen('Fractal Tree')

turtle.left(90)
turtle.pendown()

fractal_tree(150)

turtle.update()
print('Done')
turtle.done()
