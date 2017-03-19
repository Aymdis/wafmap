#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'Citrix NetScaler'


def is_waf(respDict):
    """
    First checks if a cookie associated with Netscaler is present,
    if not it will try to find if a "Cneonction" or "nnCoection" is returned
    for any of the attacks sent
    """
    # NSC_ and citrix_ns_id come from David S. Langlands <dsl 'at' surfstar.com>
    if match_type.match_header(respDict,('Set-Cookie','^(ns_af=|citrix_ns_id|NSC_)')):
        return True
    if match_type.match_header(respDict,('Cneonction', 'close')):
        return True
    if match_type.match_header(respDict,('nnCoection', 'close')):
        return True
    if match_type.match_header(respDict,('Via', 'NS-CACHE')):
        return True
    if match_type.match_header(respDict,('X-Client-IP', '.')):
        return True
    if match_type.match_header(respDict,('Set-Cookie','^pwcount')):
        return True
    return False
