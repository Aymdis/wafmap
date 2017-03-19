# -*- coding: utf-8 -*-
__author__ = "SadLin"

#refer http://www.d99net.net/

from lib.match_rule import match_type
import re
NAME = "D dun"

def is_waf(respDict):

    if  respDict["iis_shortname"] != None:
        iis_shortname_resp = respDict["iis_shortname"]
        if iis_shortname_resp.status_code == 200 and len(iis_shortname_resp.content) == 929:
            if re.findall(r"\<title\>(D).+?\</title\>",iis_shortname_resp.content)[0] =="D":
                return True
    if match_type.match_header(respDict,("Set-Cookie","^_D_SID=")):
        return True
    if match_type.match_header(respDict,("Cookie","_D_SID=")):
        return True
    return False

