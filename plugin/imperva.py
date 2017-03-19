#!/usr/bin/env python
__author__ = "SadLin"

from lib.match_rule import match_type
import socket
import urlparse

socket.setdefaulttimeout(30)
NAME = 'Imperva SecureSphere'


def is_waf(respDict):
    # thanks to Mathieu Dessus <mathieu.dessus(a)verizonbusiness.com> for this
    # might lead to false positives so please report back to sandro@enablesecurity.com
    url_param = urlparse.urlparse(respDict['normal'].url)
    host = url_param.netloc
    if url_param.port:
        port = url_param.port
    else:
        port=80
    path = url_param.path
    xss_payload = '''GET %s/?%s\n''' % (path,"<script>alert(1)</script>")
    use_agent = '''user-agent: User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36\n\n'''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))
        s.send(xss_payload)
        s.send(use_agent)
        buf = s.recv(1024)
        import re
        Httpversion  = re.match(r"HTTP/(.+?) ", buf)[0]
        if Httpversion:
            if Httpversion == '10':
                return True
    except:pass

    return False
