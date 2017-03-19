# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type

NAME = "BlockDoS"

def is_waf(respDict):
    if match_type.match_header(respDict,("Server","BlockDos\.net")):
        return True
    return  False