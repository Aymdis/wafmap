#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'F5 BIG-IP LTM'


def is_waf(respDict):
    detected = False
    if match_type.match_header(respDict,('Set-Cookie','^BIGipServer')):
        return True
    elif match_type.match_header(respDict,('X-Cnection', '^close$')):
        return True
    else:
        return False
