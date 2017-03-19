# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type

NAME  = "Newdefend Web Application Firewall (Newdefend)"

def is_waf(respDict):
    if match_type.match_header(respDict,("Sever","newdefend")):
        return True
    return False