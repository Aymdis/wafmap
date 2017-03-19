#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type


NAME = 'Microsoft ISA Server'


def is_waf(respDict):
    invalidhostresp = respDict['invalidHost']
    if match_type.match_content({'invalidhost':invalidhostresp},"The server denied the specified Uniform Resource Locator (URL). Contact the server administrator"):
        return True
    if match_type.match_content({'invalidhost':invalidhostresp},"The ISA Server denied the specified Uniform Resource Locator (URL)"):
        return True
    return False
