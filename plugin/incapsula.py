#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'Incapsula WAF'


def is_waf(respDict):
    # credit goes to Charlie Campbell
    if match_type.match_header(respDict,('Set-Cookie','^.incap_ses')):
        return True
    if match_type.match_header(respDict,('Set-Cookie','^visid.*=')):
        return True
    # https://www.zoomeye.org/search?t=host&q=X-CDN+Incapsula
    if match_type.match_header(respDict,('X-CDN','Incapsula')):
        return True
    return False
