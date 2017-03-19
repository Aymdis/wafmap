#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type
import requests

NAME = 'Better WP Security'


def is_waf(respDict):
    normalRespone = respDict['normal']
    if "Link" in normalRespone.headers.keys():
        link_header = normalRespone.headers['Link']
    else:
        link_header = ""

    if "https://api.w.org/" not in link_header:
        # Does not appear to be a wordpress at all
        return False

    resp = requests.get(normalRespone.url + "/wp-content/plugins/better-wp-security/")

    if resp.status_code != 404:
        return True
    else:
        return  False
