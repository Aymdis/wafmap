#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'F5 Trafficshield'


def is_waf(respDict):
    for g in [('cookie', '^ASINFO='), ('Server', 'F5-TrafficShield')]:
        if match_type.match_header(respDict,g):
            return True
    # the following based on nmap's http-waf-fingerprint.nse
    return False
