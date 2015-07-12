#!/usr/bin/env python

import argparse
import logging

Usage = """python alignment.py --config <config_file> --plugins \
<plugin1> <plugin2>...<pluginN> --time <time>
        """
class CmdlineParser(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(usage=Usage)
        self._config_file = None
        self._plugins = None
        self._ticks = None

    def parse(self):
        self.parser.add_argument("--config", dest='config_file', help='system configuration file for the planets')
        self.parser.add_argument("--plugins", nargs='+', dest='plugins', help="list of plugins that needs to applied on")
        self.parser.add_argument("--time", dest="ticks", type=int, help="the time after which we need to measure the alignments")
        args = self.parser.parse_args()
        logging.info("system conf file ", args)
        if args.config_file:
            self._config_file = args.config_file
        if args.plugins:
            self._plugins = args.plugins
        if args.ticks:
            self._ticks = args.ticks

    def get_config_file(self):
        return self._config_file

    def get_plugins_list(self):
        return self._plugins

    def get_ticks(self):
        return self._ticks

