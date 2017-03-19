# -*- coding: utf-8 -*-
__author__ = "SadLin"
from lib.match_rule import match_type

#创宇加速乐 KS WAF
NAME = "KS-WAF"

def is_waf(respDict):
    if match_type.match_content(respDict,"url\('/ks-waf-error\.png'\)"):
        return True