# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type

#创宇加速乐 CDN
NAME = "Jiasule Web Application Firewall"

def is_waf(respDict):
    if match_type.match_header(respDict,("Server","jiasule-WAF")):
        return True
    if match_type.match_header(respDict,("Set-Cookie","__jsluid=")):
        return True
    if match_type.match_content(respDict,"static\.jiasule\.com/static/js/http_error\.js"):
        return True