#!/usr/bin/env python
from __future__ import print_function
from planet import Planet
from input_parser import InputParser
from alignment_exceptions import AlignmentInputError
import logging

class ArbitarySolarSystem(object):
    def __init__(self, config=None):
        """ Sets up the Aribtary Solar System

        Args:
            config - config file which contains information about planets
        """
        self.planets = {}
        if config:
            ip = InputParser(config)
            try:
                planets = ip.get_objects()
                for planet in planets:
                    logging.info('planet info: ', planet)
                    p = Planet(planet['name'], planet['theta'], planet['radius'],
                            planet['period'])
                    self.planets[planet['name']] = p
            except IOError as e:
                raise AlignmentInputError("Failed to parse config file")
        else:
            logging.warning('No configuration for AribtarySolar System')

    def __str__(self):
        return "solar system of {} planets".format(len(self.planets))

    def add_planet(self, planet):
        """ Adds the planet to the solar system

        Args:
           planet - planet object which needs to be added to the solar system 
        """
        if not planet['name'] in self.planets:
            self.planets[planet['name']] = planet

    def remove_planet(self, planet):
        """ Removes the planet from the solar system

        Args:
           planet - planet object which needs to be removed from the solar system 
        """
        if planet['name'] in self.planets:
            del self.planets[planet['name']]

    def get_planets_angle(self, ticks=0):
        """ Gets the planet angle

        Args:
           ticks - time in ticks 

        Returns:
           Returns the tuple of all planets name and their angle
        """
        planets = []
        for p in self.planets.values():
           planets.append((p.name, p.get_angle_after_ticks(ticks)))   
        return tuple(planets)

#main
if __name__ == '__main__':
    ab_solar_system = ArbitarySolarSystem(config='system.yaml') 
    planets_info = ab_solar_system.get_planets_angle(10)
    for p in planets_info:
        print(p[0], p[1])
    try:
        ab_solar_system = ArbitarySolarSystem(config="system.html")
    except AlignmentInputError as e:
        print(e.msg)
    try:
        ab_solar_system = ArbitarySolarSystem(config="system_invalid.yaml")
    except AlignmentInputError as e:
        print(e.msg)

