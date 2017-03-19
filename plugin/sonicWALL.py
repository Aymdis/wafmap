# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type
#https://www.sonicwall.com/cn-zh/
NAME = "SonicWALL Firewall"

def is_waf(respDict):
    if match_type.match_header(respDict,("Server","SonicWALL")):
        return True
    if match_type.match_content(respDict,"This request is blocked by the SonicWALL"):
        return True
    if match_type.match_content(respDict,"Web Site Blocked") and match_type.match_content(respDict,"document.getElementById(\"nsa_banner"):
        return True
    return False
