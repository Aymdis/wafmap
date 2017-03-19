#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type
import requests

NAME = 'eEye Digital Security SecureIIS'


def is_waf(respDict):
    normalResp = respDict['normal']
    headers = dict()
    headers['Transfer-Encoding'] = 'z'*1025
    headers['Accept-Encoding']="identity"   # from sqlmap waf
    resp = requests.get(normalResp.url,headers=headers,verify=False)
    if resp.status_code == 404 and normalResp.status_code != 404:
        return True
    return  False
    '''
    wafw00f detection script
    # credit goes to W3AF
    detected = False
    r = self.normalrequest()
    if r is None:
        return
    response, responsebody = r
    if response.status == 404:
        return
    headers = dict()
    headers['Transfer-Encoding'] = 'z' * 1025
    r = self.normalrequest(headers=headers)
    if r is None:
        return
    response, responsebody = r
    if response.status == 404:
        detected = True
    return detected    '''


