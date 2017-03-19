#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type

#waf www.webray.com.cn
NAME = 'WebRay WAF'


def is_waf(respDict):
    # credit goes to Charlie Campbell
    if match_type.match_header(respDict,('DrivedBy','^RaySrv')):
        return True
    if match_type.match_header(respDict,('RayEngine','.')):
        return True
    return False