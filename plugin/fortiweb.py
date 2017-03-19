# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type

NAME = "FortiWeb Web Application Firewall (Fortinet Inc.)"

def is_waf(respDict):
    if match_type.match_status_header(respDict,("Set-Cookie","\AFORTIWAFSID=")):
        return True
    return False