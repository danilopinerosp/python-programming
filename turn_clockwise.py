#!/usr/bin/env python3

def turn_clockwise(point):
    ''' Takes one the the four compass points as its parameter, and returns the next compass point in the
    clockwise direction'''
    
    points = ['N', 'E', 'S', 'W']
    point = point.upper()
    if point not in points:
        return None
    if point == points[0]:
        return points[1]
    if point == points[1]:
        return points[2]
    if point == points[2]:
        return points[3]
    if point == points[3]:
        return points[0]


if __name__ == "__main__":
    point = input("Point>> ")
    result = turn_clockwise(point)
    print(result)



    
