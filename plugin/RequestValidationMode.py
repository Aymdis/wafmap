# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type

NAME =  "ASP.NET RequestValidationMode (Microsoft)"

def is_waf(respDict):
    if match_type.match_content(respDict,"ASP.NET has detected data in the request that is potentially dangerous"):
        return True
    if match_type.match_content(respDict,"Request Validation has detected a potentially dangerous client input value"):
        return True
    return False