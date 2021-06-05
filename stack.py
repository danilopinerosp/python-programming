#!/usr/bin/env python3

class Stack(object):

    def __init__(self):
        self.p = []

    def top(self):
        """ Returns the last element of the stack"""
        if not self.is_empty():
            return self.p[-1]

    def push(self, element):
        """ Push element on the top of the stack"""
        self.p = self.p + [element]

    def pop(self):
        """ Pops and returns the last element of the stack. 
        Raises an exception if the stack is empty"""
        element = self.p[-1]
        if not self.is_empty():
            self.p = self.p[:-1]
            return element
        else:
            raise Exceptio('Empty stack')

    def length(self):
        """ Returns the lenght of stack"""
        return len(self.p)

    def is_empty(self):
        """ Returns True is stack is empty, False otherwise"""
        return self.length() == 0

    def __str__(self):
        return "{}".format(self.p)

    def __repr__(self):
        return "{}".format(self.p)
        
