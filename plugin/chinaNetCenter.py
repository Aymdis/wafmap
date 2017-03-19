# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type
#网宿cdn
NAME = "chinaNetCenter CDN"

def is_waf(respDict):
    if match_type.match_header(respDict,("X-Via","Cdn Cache Server V2.0")):
        return True
    if match_type.match_header(respDict,("X-CDN-Forward","ChinaNetCenter")):
        return True

    return False