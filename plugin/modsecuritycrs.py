#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'ModSecurity (OWASP CRS)'


def is_waf(respDict):
    return False