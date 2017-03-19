# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type

NAME = "IBM WebSphere DataPower (IBM)"

def is_waf(respDict):
    if match_type.match_header(respDict,("X-Backside-Transport","\A(OK|FAIL)")):
        return True