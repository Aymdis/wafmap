#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'Barracuda Application Firewall'


def is_waf(respDict):
    # credit goes to W3AF
    if match_type.match_header(respDict,('Set-Cookie','^barra_counter_session=')):
        return True
    # credit goes to Charlie Campbell
    if match_type.match_header(respDict,('Set-Cookie','^BNI__BARRACUDA_LB_COOKIE=')):
        return True
    # credit goes to yours truly
    if match_type.match_header(respDict,('Set-Cookie','^BNI_persistence=')):
        return True
    if match_type.match_header(respDict,('Set-Cookie','^BN[IE]S_.*?=')):
        return True
    if match_type.match_status_content(respDict,(404,"The specified URL cannot be found<!--0123456789.+?-->")):
        return True
    return False
