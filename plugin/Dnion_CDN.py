# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type
#帝联cdn

NAME = "Dnion CDN"

def is_waf(respDict):
    if match_type.match_header(respDict,("Server","DnionOS")):
        return True
    if match_type.match_header(respDict,("Server-Info","DnionATS")):
        return True
    if match_type.match_header(respDict,("Via",".+?(DLC-3.0),.+?(DLC-3.0)")):
        return True
    if match_type.match_header(respDict,("Warning","DLC-3.0 ")):
        return True


    return False