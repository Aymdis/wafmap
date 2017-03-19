#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'Art of Defence HyperGuard'


def is_waf(respDict):
    # credit goes to W3AF
    if match_type.match_header(respDict,('Set-Cookie','^WODSESSION=')):
        return True
    if match_type.match_header(respDict,('Set-Cookie','^ODSESSION=')):
        return True
    return  False
