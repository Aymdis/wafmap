#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'F5 FirePass'


def is_waf(respDict):
    detected = False
    if match_type.match_header(respDict,('Location', '\/my\.logon\.php3')) and match_type.match_header(respDict,('Set-Cookies','^VHOST')):
        return True
    elif match_type.match_header(respDict,('Set-Cookies','^MRHSession')) and (match_type.match_header(respDict,('Set-Cookies','^VHOST')) or match_type.match_header(respDict,('Set-Cookies','^uRoamTestCookie'))):
        return True
    elif match_type.match_header(respDict,('Set-Cookies','^MRHSession')) and (match_type.match_header(respDict,('Set-Cookies','^MRHCId')) or match_type.match_header(respDict,('Set-Cookies','^MRHIntranetSession'))):
        return True
    elif match_type.match_header(respDict,('Set-Cookies','^uRoamTestCookie')) or match_type.match_header(respDict,('Set-Cookies','^VHOST')):
        return True
    else:
        return False
