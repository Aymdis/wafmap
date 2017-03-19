#!/usr/bin/env python
from lib.match_rule import match_type

NAME = '360WangZhanBao'


def is_waf(respDict):
    return match_type.match_header(respDict,('X-Powered-By-360WZB', '.+'))
