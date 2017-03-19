#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'CloudFlare'


# the following based on nmap's http-waf-fingerprint.nse
def is_waf(respDict):
    if match_type.match_header(respDict,('Server', 'cloudflare-nginx')):
        return True
    if match_type.match_header(respDict,('Set-Cookie','__cfduid')):
        return True
    return False
