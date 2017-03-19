# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type

NAME = "Palo Alto Firewall (Palo Alto Networks)"

def is_waf(respDict):
    if match_type.match_content(respDict,"Access[^<]+has been blocked in accordance with company policy"):
        return True
    return False
