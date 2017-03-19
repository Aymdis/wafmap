#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type
import requests

NAME = 'Microsoft URLScan'


def is_waf(respDict):
    if match_type.match_header(respDict,('Location','Rejected-By-UrlScan')): #from sqlmap
        return  True
    #refer to wafw00f
    testheaders = dict()
    testheaders['Translate'] = 'z' * 10
    testheaders['If'] = 'z' * 10
    testheaders['Lock-Token'] = 'z' * 10
    testheaders['Transfer-Encoding'] = 'z' * 10
    normalResp = respDict['normal']
    try:
        resp = requests.get(normalResp.url,headers=testheaders,verify=False)
        if resp.status_code != normalResp.status_code:
            if resp.status_code == 404:
                return  True
    except:pass
    return False
