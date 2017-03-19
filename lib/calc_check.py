# -*- coding: utf-8 -*-
__author__ = "SadLin"

import difflib
import re

#连接被阻塞或者终止
def connect_aborted(respDict):
    # waf  would aborted connection with malicious requests such https://61.57.227.29/
    if respDict['normal'] != None and respDict['xss'] == None and respDict['notExistFile'] != None:
        return True
    return False

#返回不同响应内容
def diff_status(respDict):
    # if website is not protect by waf ,the respone status  for notExistFile would the same as status_code for  malicious requests by notExistFile.
    # waf may be reactd to malicious requests by notExistFile with diffrrent status code
    try:
        if respDict['notExistFile'].status_code != respDict['xss_notExistFile'].status_code:
            return True
    except:
        pass
    return False

#响应头部变化
def diff_header(respDict):
    noServers = [('Microsoft-IIS/7.0', 'Microsoft-HTTPAPI/2.0'), ('Microsoft-HTTPAPI/2.0', 'Microsoft-IIS/7.0'),
                 ('Microsoft-IIS/8.0', 'Microsoft-HTTPAPI/2.0'), ('Microsoft-HTTPAPI/2.0', 'Microsoft-IIS/8.0')]
    Servers = []
    for resp in respDict.values():
        if resp != None:
            if "Server" in resp.headers.keys():
                if resp.headers['Server'] not in Servers:
                    Servers.append(resp.headers['Server'])
    if len(Servers) > 1 and tuple(Servers) not in noServers:
        print "[!] Diff respone header Find %s" % str(Servers)
        return True
    return False

#页面相识度计算
def diff_content(respDict):
    #test url http://cfl.fjnu.edu.cn/
    html1 = respDict['notExistFile'].content
    html2 = removeDynamicContent(respDict["xss_notExistFile"].content)
    ratio = difflib.SequenceMatcher(None,html1,html2).ratio()
    if ratio>1:
        ratio = 1/ratio
    if ratio>0.5:
        return False
    return True

#移除动态页面
def removeDynamicContent(content):
    content = re.sub(re.escape("<script>alert(1)</script>"),"",content)
    content = re.sub(re.escape("&lt;script&gt;alert(1)&lt;script&gt;"),"",content)
    return content
