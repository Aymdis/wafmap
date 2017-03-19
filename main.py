# -*- coding: utf-8 -*-
__author__ = "SadLin"
import sys
import urlparse
import optparse
from lib.calc_check import *
from lib.match_rule import match_type
from lib.load_plugins import load_plugins,show_waf_list

class checkWaf(object):
    def __init__(self,RespDict):
        self.respDict = RespDict
    #方法一:  遍历所有指纹规则
    def Fingers_travel_check(self):
        pluginsDict = {}
        pluginsDict = load_plugins()
        for plugin_module in pluginsDict.values():
            #print plugin_module.NAME
            if plugin_module.is_waf(self.respDict):
                print "[!] website is protect by : %s " % plugin_module.NAME
                if test_all:
                    continue
                return True
        return False
    #方法二: 算法计算
    def calculation_check(self):
        if connect_aborted(self.respDict):
            print "[!] malicious requests was aborted by website "
            return True
        if  diff_status(self.respDict):
            print "[!] perform diff resppne status between normal and malicous request "
            return True
        if diff_header(self.respDict):
            print "[!] perform diff resppne header between normal and malicous request "
            return True
        if diff_content(self.respDict):
            print "[!] perform diff resppne content between notExistFile and xss_notExistFile request "
            return True
        return False



if __name__ == "__main__":
    parser = optparse.OptionParser('usage: %prog [options] target.com', version="%prog 1.0")
    parser.add_option("-u","--url",dest="url",type="string",default=False,action="store",help="target url e.g:http://www.example.com/")
    parser.add_option("","--proxy",dest="proxy",type="string",default=None,action="store",help="scan proxy eg:127.0.0.1:8080")
    parser.add_option("-l","--list",dest="list",default=False,action="store_true",help="show all of the web application Firewall")
    parser.add_option("-a","--all",dest="all",default=False,action="store_true",help="test all fingers ignore an waf was identified")
    (options, args) = parser.parse_args()
    proxy = options.proxy
    global test_all
    test_all = False
    if options.all:
        test_all = True
    if options.list:
        show_waf_list()
        sys.exit(0)
    if options.url:
        url = options.url
        url_param = urlparse.urlparse(url)
        if url_param.scheme == "https":
            ssl = True
        else:
            ssl=False
        netloc = url_param.netloc
        path = url_param.path
        port = 80
        match = match_type(netloc, port, path, proxy=proxy, ssl=ssl)
        respDict = match.getRespDict()
        identifyWaf = checkWaf(respDict)
        if identifyWaf.Fingers_travel_check():
            sys.exit(0)
        if identifyWaf.calculation_check():
            print "[!] website may be protect by Waf !"
            sys.exit(0)
        print "[!] the website seem not to be protected by waf"
    else:
        parser.print_help()