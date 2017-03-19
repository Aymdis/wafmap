#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'F5 BIG-IP APM'


def is_waf(respDict):
    detected = False
    # the following based on nmap's http-waf-fingerprint.nse
    if match_type.match_header(respDict,('Set-Cookie','^LastMRH_Session')) and match_type.match_header(respDict,('Set-Cookie','^MRHSession')):
        return True
    elif match_type.match_header(respDict,('Server', 'BigIP|BIG-IP|BIGIP')) and match_type.match_header(respDict,('Set-Cookie','^MRHSession')):
        return True
    if match_type.match_header(respDict,('Location', '\/my.policy')) and match_type.match_header(respDict,('Server', 'BigIP|BIG-IP|BIGIP')):
        return True
    elif match_type.match_header(respDict,('Location', '\/my\.logout\.php3')) and match_type.match_header(respDict,('Server', 'BigIP|BIG-IP|BIGIP')):
        return True
    elif match_type.match_header(respDict,('Location', '.+\/f5\-w\-68747470.+')) and match_type.match_header(respDict,('Server', 'BigIP|BIG-IP|BIGIP')):
        return True
    elif match_type.match_header(respDict,('Server', 'BigIP|BIG-IP|BIGIP')):
        return True
    elif match_type.match_header(respDict,('Set-Cookie','^F5_fullWT')) or match_type.match_header(respDict,('Set-Cookie','^F5_ST')) or match_type.match_header(respDict,('Set-Cookies','^F5_HT_shrinked')):
        return True
    elif match_type.match_header(respDict,('Set-Cookie','^MRHSequence')) or match_type.match_header(respDict,('Set-Cookie','^MRHSHint')) or match_type.match_header(respDict,('Set-Cookie','^LastMRH_Session')):
        return True
    else:
        return False
