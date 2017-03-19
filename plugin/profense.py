#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'Profense'


def is_waf(respDict):
    """
    Checks for server headers containing "profense"
    """
    return match_type.match_header(respDict,('Server', 'profense'))
