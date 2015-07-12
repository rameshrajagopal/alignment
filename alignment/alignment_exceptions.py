#!/usr/bin/env python

class AlignmentError(Exception):
    pass

class AlignmentInputError(AlignmentError):
    """Exception raised for the errors in the input

     Attributes:
        msg - explanation of the error
    """
    def __init__(self, msg):
        self.msg  = msg
