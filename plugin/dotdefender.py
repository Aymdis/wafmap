#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'Applicure dotDefender'


def is_waf(respDict):
    if  match_type.match_header(respDict,('X-dotDefender-denied', '^1$')):
        return True
    if match_type.match_content(respDict,'dotDefender Blocked Your Request'):
        return True
    return False
