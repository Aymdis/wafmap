#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'BinarySec'


def is_waf(respDict):
    # credit goes to W3AF
    if match_type.match_header(respDict,('Server', 'BinarySec')):
        return True
    # the following based on nmap's http-waf-fingerprint.nse
    elif match_type.match_header(respDict,('x-binarysec-via', '.')):
        return True
    # the following based on nmap's http-waf-fingerprint.nse
    elif match_type.match_header(respDict,('x-binarysec-nocache', '.')):
        return True
    else:
        return False
