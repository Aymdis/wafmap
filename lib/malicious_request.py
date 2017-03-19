# -*- coding: utf-8 -*-
__author__ = "SadLin"
import random
import requests
import  urllib
requests.packages.urllib3.disable_warnings()


# 发送恶意请求,触发防火墙进行响应,返回可匹配规则。
class request_payloads(object):
    def __init__(self,host,port,path,proxy=None,ssl=False):
        pass
    #合法正常的请求,此响应结果可用来做对比
    def normal_request(self):
        return requests.get(self.targetUrl,headers=self.header,verify=False,proxies=self.proxy)

    def nonexistent_File_request(self):
        try:
            return requests.get(self.targetUrl+'/'+self.nonexistent_File_payload, headers=self.header, verify=False, proxies=self.proxy)
        except Exception,e:
            pass
        return

    def xss_nonexistent_File_request(self):
        try:
            return requests.get(self.targetUrl+'/'+self.xss_nonexistent_File_payload, headers=self.header, verify=False, proxies=self.proxy)
        except Exception,e:
            pass
        return

    def xss_requests(self):
        try:
            return requests.get(self.targetUrl + "/?Paylo4d=" + self.xss_paylod, headers=self.header, verify=False,proxies=self.proxy)
        except Exception,e:
            pass
        return

    def xss_encode_request(self):
        try:
            return requests.get(self.targetUrl + "/?Paylo4d=" + urllib.quote(self.xss_paylod), headers=self.header, verify=False,proxies=self.proxy)
        except Exception,e:
            pass
        return

    def protectDir_request(self):
        try:
            return  requests.get(self.targetUrl + "/?Paylo4d=" + self.protectDir_payload, headers=self.header, verify=False,proxies=self.proxy)
        except Exception,e:
            pass
        return

    def dirtravel_request(self):
        try:
            return requests.get(self.targetUrl + self.dirtravel_payload, headers=self.header, verify=False,proxies=self.proxy)
        except Exception,e:
            pass
        return

    def dirtravel_encode_request(self):
        try:
            return requests.get(self.targetUrl + urllib.quote(self.dirtravel_payload), headers=self.header, verify=False,proxies=self.proxy)
        except Exception,e:
            pass
        return

    def invalidHost_request(self):
        try:
            return  requests.get(self.targetUrl,headers={"HOST":str(random.randrange(100000, 999999))},verify=False,proxies=self.proxy)
        except Exception,e:
            pass
        return
    def iis_shortname_request(self):
        try:
            return requests.get(self.targetUrl +self.iis_shortname_payload, headers=self.header, verify=False,proxies=self.proxy)
        except Exception,e:
            pass
        return



    @classmethod
    def selfRequest(self,url,max_time):
        resp = requests.get(url,data="'<script>alert(xss)</script>"+str(random.randint(1000,9999)*"a"),timeout=max_time)

    @classmethod
    def dos_request(self,targetUrl):
        import threading
        threads = []
        for i in xrange(100):
            i += 1
            t= threading.Thread(target=requests.get,args=(targetUrl,))
            threads.append(t)
        for t in threads:
            t.setDaemon(True)
            t.start()
        for t in threads:
            try:
                t.join(45)
            except Exception,e:
                return True
        return False

