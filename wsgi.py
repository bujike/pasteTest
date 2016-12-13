#! /usr/lib/env python
# -*- coding: utf-8 -*-
'''
Created on 2011-6-12
@author: Sonic
'''
import os
from paste.deploy import loadapp
from wsgiref.simple_server import make_server


configfile = "/etc/pasteTest/paste.ini"
appname = "pdl"
# wsgi_app = loadapp("config:%s" % os.path.abspath(configfile), appname)
application = loadapp("config:%s" % os.path.abspath(configfile), appname)
if __name__ == '__main__':
    #测试
    server = make_server('192.168.13.234', 8080, application)
    server.serve_forever()
else:

    pass