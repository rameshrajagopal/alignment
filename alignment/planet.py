#!/usr/bin/env python
from __future__ import print_function
from math import pi as PI

class Planet(object):
    def __init__(self, name, theta, radius, period):
        """ Creats a Planet object.
        Args:
            name : Name of the planet
            theta : Angle of the planet in radians
            radius : Radius from the sun that the planet orbits
            period : Length of the time it takes to orbit the sun, in
            milliseconds- 
        """
        self.name  = name
        self.theta = theta
        self.radius = radius            
        self.period = period

    def __str__(self):
        return  self.name

    def move(self, ticks):
        """planet angle will be moved based on ticks
        Args:
           ticks - move the planet upto ticks time
        """
        ticks = ticks % self.period
        self.theta = self.theta + (2 * PI * ticks)/self.period

    def get_angle_after_ticks(self, ticks):
        """ Get the planet angle after the elapse of ticks from the init
            position
        Args: 
            ticks - the time in milliseconds
        Returns:
            The angle of the planet after ticks time.
        """
        ticks = ticks % self.period
        theta = self.theta + (2 * PI * ticks)/self.period
        return theta

#test function for Planet
if __name__ == '__main__':
    init_angle = 0
    period = 20
    p = Planet('PlanetA', init_angle, 5, period)
    angle = p.get_angle_after_ticks(20)
    if angle != 0:
        print("FAILED")
    else:
        print("PASS")
    angle = p.get_angle_after_ticks(30)
    if angle != PI:
        print("FAILED %d" % angle)
    else:
        print("PASS")
    angle = p.get_angle_after_ticks(5)
    if angle != (PI/2):
        print("FAILED %d" % angle)
    else:
        print("PASS")

            
