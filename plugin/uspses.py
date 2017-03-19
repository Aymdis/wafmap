#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'USP Secure Entry Server'


def is_waf(respDict):
    if match_type.match_header(respDict,('Server', 'Secure Entry Server')):
        return True
    return False
