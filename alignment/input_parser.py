#!/usr/bin/env python
from alignment_exceptions import AlignmentInputError
import logging

class InputParser(object):
    def __init__(self, filename):
        """Creates InputParser object

        Args:
            filename : input file for parsing
        """
        self.filename = filename

    def get_objects(self):
        """Parses the file and returns the objects

        Returns: 
            Returns all the input objects as a list
            Raises exception if the input fileformat doesn't match 
        """
        if self.filename.endswith(".yaml"):
            import yaml
            try:
                with open(self.filename) as f:
                    conf = yaml.load(f)
                    if not 'system' in conf:
                        raise AlignmentInputError('config file does not have system header')
                    logging.info('conf file:\n', conf['system'])
                    return conf['system']
            except IOError as e:
                logging.error(str(e))
                raise e
        else:
           raise AlignmentInputError('invalid config file format')

#main
if __name__ == '__main__':
    ip = InputParser('system.yaml')
    conf_objects = ip.get_objects()
    print(conf_objects)
    ip = InputParser('system1.yaml')
    conf_objects = ip.get_objects()
    print(conf_objects)