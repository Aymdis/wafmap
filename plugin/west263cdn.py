#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'West263CDN'


def is_waf(respDict):
    return match_type.match_header(respDict,('X-Cache', '.+WT263CDN-.+'))
