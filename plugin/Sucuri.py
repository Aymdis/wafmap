# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type

NAME = "Sucuri WebSite Firewall"

def is_waf(respDict):
    if match_type.match_status_header(respDict,(403,"Server","Sucuri/Cloudproxy")):
        return True
    return False