#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'Teros WAF'


def is_waf(respDict):
    # credit goes to W3AF
    return match_type.match_header(respDict,('Set-Cookie','^st8(id|_wat|_wlf)='))
