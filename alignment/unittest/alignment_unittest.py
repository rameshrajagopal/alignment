#!/usr/bin/env python

import unittest
#include this in the executing path
import os.path, sys
sys.path.extend(['..', '.'])
from planet import Planet
from input_parser import InputParser
from math import pi as PI
from alignment_exceptions import AlignmentInputError

class TestPlanetModule(unittest.TestCase):
    """ Class to test Planet Module """ 
    def setUp(self):
        self.theta = 0
        self.radius = 10
        self.period  = 32
        self.planet = Planet('planet-A', self.theta, self.radius, self.period)

    def test_planet_angles_after_ticks(self):
        angle = self.planet.get_angle_after_ticks(self.period/2)
        self.assertEqual(angle, self.theta + PI, 'wrong angle after ticks')

    def test_planet_angles_after_ticks_invalid_value(self):
        angle = self.planet.get_angle_after_ticks(-1)
        self.assertEqual(angle, None)

    def test_planet_angles_after_ticks_after_move(self):
        self.planet.move(self.period/4)
        angle = self.planet.get_angle_after_ticks(self.period/2)
        self.assertEqual(angle, self.theta + (3 * PI)/2, 'wrong angle after move')

class TestInputParser(unittest.TestCase):
    ''' Tests the input parser which parse yaml file '''
    def test_input_parser_with_file(self):
        ip = InputParser('../configs/sample.yaml')
        conf = ip.get_objects()
        self.assertEqual(len(conf), 4, 'wrong parsing has been done')

    def test_input_parser_with_wrong_file(self):
        ip = InputParser('sampl.yaml')
        try:
            conf = ip.get_objects()
            self.assertEqual(conf, None, 'Wrong input parser')
        except IOError as e:
            self.assertEqual(None, None)

    def test_input_parser_with_wrong_values(self):
        ip = InputParser('../configs/sample_invalid.yaml')
        try:
            conf = ip.get_objects()
            self.assertEqual(conf, None, 'Wrong parsing is done')
        except AlignmentInputError as e:
            self.assertEqual(None, None)

    def test_input_parser_with_wrong_values(self):
        ip = InputParser('../configs/sample_invalid_tag.yaml')
        try:
           conf = ip.get_objects()
           self.assertEqual(conf, None, 'Wrong parsing is done')
        except AlignmentInputError as e:
           self.assertEqual(None, None)


#main
if __name__ == '__main__':
    unittest.main()
