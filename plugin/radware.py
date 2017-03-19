# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type

NAME =  "AppWall (Radware)"

def is_waf(respDict):
    if match_type.match_content(respDict,"Unauthorized Activity Has Been Detected.+Case Number:"):
        return True
    if match_type.match_header(respDict,("X-SL-CompState",".")):
        return True
    return False
