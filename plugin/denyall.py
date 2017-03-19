#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'DenyALL WAF'


def is_waf(respDict):
    # credit goes to W3AF
    if match_type.match_header(respDict,('Set-Cookie','^sessioncookie=')):
        return True
    # credit goes to Sebastien Gioria
    #   Tested against a Rweb 3.8
    # and modified by sandro gauci and someone else
    if match_type.match_status_reason(respDict,(200,'Condition Intercepted')):
        return True

    return False
