# -*- coding: utf-8 -*-
__author__ = "SadLin"


from lib.match_rule import match_type
#refer http://www.weidun.com.cn/
NAME = 'Weidun IIS Web Firewall'

def is_waf(respDict):
    if match_type.match_header(respDict,("Firewall","www.weidun.com.cn")):
        return True
    if match_type.match_header(respDict,("Server","WeiDun IIS Firewall")):
        return True
    return False
