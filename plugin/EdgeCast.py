# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type

NAME = "EdgeCast WAF (Verizon)"

def is_waf(respDict):
    if match_type.match_status_header(respDict,(400,"Server","\AECDF")):
        return True
    return False