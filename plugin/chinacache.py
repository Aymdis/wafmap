#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'ChinaCache-CDN'


def is_waf(respDict):
    return match_type.match_header(respDict,('Powered-By-ChinaCache', '.+'))
