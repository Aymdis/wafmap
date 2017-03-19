# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type

NAME = 'Safe3 Web Firewall'

#test http://180.131.50.234/

def is_waf(respDict):
    if match_type.match_header(respDict,("Server","Safe3 Web Firewall")):
        return True
    if match_type.match_header(respDict,("X-Powered-By","Safe3WAF/\d\.\d\.\d")):
        return True
    return  False

