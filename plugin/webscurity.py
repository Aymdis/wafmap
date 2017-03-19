#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type
import urlparse
import requests

NAME = 'Juniper WebApp Secure'


def is_waf(respDict):
    #refer wafw00f
    normalResp = respDict['normal']
    if normalResp.status_code == 403:
        return False
    url_param = urlparse.urlparse(normalResp.url)
    url =url_param.scheme+"://"+url_param.netloc+"/"+url_param.path+"?nx=@@"
    resp = requests.get(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"},verify=False)
    if resp.status_code == 403:
        return True
    return False

