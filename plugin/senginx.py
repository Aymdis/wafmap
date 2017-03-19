# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type

NAME = "SEnginx (Neusoft Corporation)"

def is_waf(respDict):
    if match_type.match_content(respDict,"SENGINX-ROBOT-MITIGATION"):
        return True
    return False
