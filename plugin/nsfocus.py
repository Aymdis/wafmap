#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'NSFocus'


def is_waf(respDict):
    if match_type.match_header(respDict,('Server', 'NSFocus')):
        return True
    return False
