# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type
NAME = "Varnish FireWall (OWASP) "

def is_waf(respDict):
    if match_type.match_header(respDict,("X-Varnish",".")):
        return True
    if match_type.match_header(respDict,("Via","varnish\Z")):
        return True
    return False