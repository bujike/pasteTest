#! /usr/lib/env python
# -*- coding: utf-8 -*-
from webob.dec import wsgify
from webob import Request
from webob import Response
# Filter
class LogFilter2():
    def __init__(self, app):
        print 'logfilter2'
        self.app = app
        pass

    def __call__(self, environ, start_response):
        print "filter:LogFilter2 is called."
        return self.app(environ, start_response)

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print "in LogFilter2.factory", global_conf, kwargs
        return LogFilter2
