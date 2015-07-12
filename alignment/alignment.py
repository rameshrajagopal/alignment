#!/usr/bin/env python
from __future__ import print_function
from cmdline_parser import CmdlineParser, Usage
from arbitory_solar_system import ArbitarySolarSystem
from alignment_exceptions import AlignmentInputError
import importlib
import os.path
import sys
import logging

def load_plugin(plugin):
    dirname = os.path.abspath(os.path.dirname(plugin))
    module  = os.path.basename(plugin).split('.')[0]
    plugin_module = None
    logging.info('plugin dirname: {}'.format(dirname))
    logging.info('plugin modulename: {}'.format(module))
    try:
        sys.path.append(dirname)
        plugin_module = importlib.import_module(module)#, package=os.path.abspath(dirname))
    except ImportError as e:
        logging.warning('Module {} is not found'.format(module))
    return plugin_module

def main_application():
    parser = CmdlineParser()
    parser.parse()
    #input required parameters
    config_file = parser.get_config_file()
    plugins = parser.get_plugins_list()
    time    = parser.get_ticks()
    if config_file is None or plugins is None:
        print(Usage)
        sys.exit(-1)
    if time is None:
        time = 0
    #setup solar system
    try:
        solar_system = ArbitarySolarSystem(config_file)
    except AlignmentInputError as e:
        logging.error(e.msg)
        sys.exit(-1)
    planets_info = solar_system.get_planets_angle(ticks=time)
    for plugin in plugins:
        plugin_mod = load_plugin(plugin)
        if plugin_mod and hasattr(plugin_mod, 'print_alignment'):
            plugin_mod.print_alignment(planets_info)
        else:
            print("plugin doesn't support print_alignement method")

#main method
if __name__ == '__main__':
    main_application()
