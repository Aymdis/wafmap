#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'Aqtronix WebKnight'


def is_waf(respDict):
    if match_type.match_status_reason(respDict,(999,"No Hacking")):
        return True
    if match_type.match_header(respDict,('Server','WebKnight')):
        return True
    return False
