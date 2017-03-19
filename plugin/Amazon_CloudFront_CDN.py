# -*- coding: utf-8 -*-
__author__ = "SadLin"

from lib.match_rule import match_type

NAME = "Amazon CloudFront CDN"

def is_waf(respDict):
    if match_type.match_header(respDict,("x-amz-id-2",".")):
        return True
    if match_type.match_header(respDict,("x-amz-request-id",".")):
        return True
    if match_type.match_header(respDict,("Server","Amazon")):
        return True
    if match_type.match_header(respDict,("X-Amz-Cf-Id",".")):
        return True
    if match_type.match_header(respDict,("X-Cache"," from cloudfront")):
        return True
    if match_type.match_header(respDict,("Via","cloudfront.net (CloudFront)")):
        return True

    return False