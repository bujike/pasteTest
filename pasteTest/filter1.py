#! /usr/lib/env python
# -*- coding: utf-8 -*-
from webob.dec import wsgify
from webob import Request
from webob import Response


# Filter
class LogFilter():
    def __init__(self, app):
        print 'logfilter1'
        self.app = app
        pass
    @wsgify
    def __call__(self, req):
        print "filter:LogFilter is called."
        return req.get_response(self.app)
    # def __call__(self, environ, start_response):
    #     print "filter:LogFilter is called."
    #     return self.app(environ, start_response)

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print "in LogFilter.factory", global_conf, kwargs
        return LogFilter

