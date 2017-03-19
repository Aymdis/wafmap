#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'F5 BIG-IP ASM'


def is_waf(respDict):
    # credit goes to W3AF
    return match_type.match_header(respDict,('Set-Cookie','^TS[a-zA-Z0-9]{3,8}='))
