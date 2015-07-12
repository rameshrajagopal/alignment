#!/usr/bin/env python
from __future__ import print_function
from math import pi as PI
try:
    from future_builtins import zip as izip
except ImportError:
    try:
        from itertools import izip
    except ImportError:
        from builtins import zip as izip
from itertools import tee

def pairwise(iterable):
    """ Returns the pairwise seq of iterable"""
    a, b = tee(iterable)
    next(b, None)    
    return izip(a, b)

def get_angle(planet):
    """get the angle in radians and convert it into degrees
       it also puts all the planets within 180 degrees
    """
    angle_in_radians = planet[1]
    angle_in_degrees = ((2 * PI)/360) * angle_in_radians
    return (angle_in_degrees % 180)

def print_alignment(planets):
    '''This will print the alignments of the planet within 5 degrees

    Args:
        planets - tuple of tuple(name, angle) in radians
    '''
    planets = sorted(planets, key=get_angle)
    degree_diff = 0
    alignment_list = []
    for e in pairwise(planets):
        if (e[1][1] - e[0][1]) <= degree_diff:
            alignment_list.append(e[0][0])
            alignment_list.append(e[1][0])
    alignment_set = set(alignment_list) 
    print("%s: " % __name__, end=" ")
    set_iterator = alignment_set.__iter__()
    e = next(set_iterator, None)
    if e:
        print("%s" % e, end="")
        while e:
           e = next(set_iterator, None)
           if e:
               print(",", end=" ")
               print("%s" % e, end="")
           else:
               print("")
