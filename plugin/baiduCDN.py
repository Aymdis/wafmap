# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type

NAME = "Yunjiasu Web Application Firewall (YunDun or baidu Cdn)"

def is_waf(respDict):
    if match_type.match_header(respDict,("X-Server","fhl")):
        return True
    if match_type.match_header(respDict,("Server","yunjiasu-nginx")):
        return True
    return False