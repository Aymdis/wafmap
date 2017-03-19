#!/usr/bin/env python
from lib.match_rule import match_type

NAME = 'Safedog'

def is_waf(respDict):
    if match_type.match_header(respDict,('Set-Cookie','^safedog-flow-item=')):
        return True
    if match_type.match_header(respDict,('Server', '^Safedog')):
        return True
    if match_type.match_header(respDict,('X-Powered-By', '^WAF/\d\.\d')):
        return True
    return False
