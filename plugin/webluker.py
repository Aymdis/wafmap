# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type
#refer 蓝汛CDN http://www.webluker.com/

NAME = "WeblukerCDN"

def is_waf(respDict):
    if match_type.match_header(respDict,("Webluker-Edge",".")):
        return True
    return False