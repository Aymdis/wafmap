# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type

NAME = "Proventia Web Application Security (IBM)"

def is_waf(respDict):
    if respDict['normal'] is None:
        return False
    if respDict['protectDir'] is None:
        return True
    return False