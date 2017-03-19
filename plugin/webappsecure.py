# -*- coding: utf-8 -*-
__author__ = "SadLin"
from lib.match_rule import match_type
import requests
NAME = "webApp.secure (webScurity)"

def is_waf(respDict):
    if respDict['normal'].headers == 403:
        return False
    try:
        resp = requests.get(respDict['normal'].url+"?nx=@@",verify=False)
        if resp.status_code == 403:
            return True
    except:
        pass
    return False