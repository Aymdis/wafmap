#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'Cisco ACE XML Gateway'


def is_waf(respDict):
    if match_type.match_header(respDict,('Server', 'ACE XML Gateway')):
        return True
    return False
