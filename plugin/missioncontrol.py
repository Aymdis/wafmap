#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'Mission Control Application Shield'


def is_waf(respDict):
    if match_type.match_header(respDict,('Server', 'Mission Control Application Shield')):
        return True
    return False
