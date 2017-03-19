# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type

#https://www.akamai.com/us/en/solutions/products/cloud-security/kona-site-defender.jsp

NAME = "KONA Security Solutions (Akamai Technologies)"

def is_waf(respDict):
    if match_type.match_status_content(respDict,(400,"Reference #[0-9A-Fa-f.]+")):
        return True
    return False