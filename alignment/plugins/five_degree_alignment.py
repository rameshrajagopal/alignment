#!/usr/bin/env python
from __future__ import print_function
from math import pi as PI

def get_angle(planet):
    angle_in_radians = planet[1]
    angle_in_degrees = ((2 * PI)/360) * angle_in_radians
    return angle_in_degrees

def print_alignment(planets):
    '''This will print the alignments of the planet within 5 degrees

    Args:
        planets - tuple of tuple(name, angle) in radians
    '''
    planets = sorted(planets, key=get_angle)
    print("%s:" % __name__, end=" ")
    for p in planets: 
        print(p[0], end=", ")
