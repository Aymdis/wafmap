#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'InfoGuard Airlock'


def is_waf(respDict):
    # credit goes to W3AF
    return match_type.match_header(respDict,('Set-Cookie','^AL[_-]?(SESS|LB))='))
