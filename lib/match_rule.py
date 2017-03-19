# -*- coding: utf-8 -*-
__author__ = "SadLin"

import re
import random
from malicious_request import  request_payloads
class match_type(request_payloads):
    def __init__(self,host,port=80,path="/",proxy=None,ssl=False):
        self.nonexistent_File_payload = str(random.randint(10000,99999))+".html"
        self.xss_paylod = "<script>alert(1)</script>"
        self.dirtravel_payload = "../../../../../etc/passwd"
        self.protectDir_payload = "/Admin_Files/"
        self.xss_nonexistent_File_payload = self.xss_paylod+self.nonexistent_File_payload
        self.iis_shortname_payload = "/*~1*/.aspx"
        self.host = host
        self.port = port
        self.path = path
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"}
        self.proxy = proxy
        self.ssl = ssl
        if self.ssl:
            self.targetUrl = "https://"+self.host+self.path
        else:
            self.targetUrl = "http://"+self.host+self.path
            print self.targetUrl

    def getRespDict(self):
        respDict = {}
        respDict["normal"] = self.normal_request()
        respDict["xss"] = self.xss_requests()
        respDict["xssEncode"] = self.xss_encode_request()
        respDict["dirtravel"] = self.dirtravel_request()
        respDict["dirEncode"] = self.dirtravel_encode_request()
        respDict["protectDir"] = self.protectDir_request()
        respDict["notExistFile"] = self.nonexistent_File_request()
        respDict["invalidHost"] = self.invalidHost_request()
        respDict["xss_notExistFile"] = self.xss_nonexistent_File_request()
        respDict["iis_shortname"] = self.iis_shortname_request()
        return respDict

    @classmethod
    def match_header(self,respDict,fingerRule):
        for respone in respDict.values():
            try:
                keyString = respone.headers[fingerRule[0]]
                if re.findall(fingerRule[1],keyString,re.IGNORECASE):
                    return True
            except:
                pass

        return  False

    @classmethod
    def match_content(self,respDict,fingerRule):
        for respone in respDict.values():
            try:
                if re.findall(fingerRule,respone.content,re.IGNORECASE):
                    return True
            except:
                pass
        return False

    #match status and reason phrase 匹配响应码和响应码描述
    @classmethod
    def match_status_reason(self,respDict,fingerRule):
        try:
            for respone in  respDict.values():
                if respone.status_code == fingerRule[0] and respone.reason == fingerRule[1]:
                    return True
            return  False
        except:
            pass

    @classmethod
    def match_status_content(self,respDict,fingerRule):
        for respone in  respDict.values():
            try:
                if respone.status_code == fingerRule[0]:
                    if re.findall(fingerRule[1],respone.content,re.IGNORECASE):
                        return True
            except:
                pass
        return  False

    @classmethod
    def match_status_header(self,respDict,fingerRule):
        for respone in respDict.values():
            try:
                if respone.status_code == fingerRule[0]:
                    keyString = respone.headers[fingerRule[1]]
                    if re.findall(fingerRule[2],keyString,re.IGNORECASE):
                        return True
            except:
                pass

        return  False