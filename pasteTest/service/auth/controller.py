#! /usr/lib/env python
# -*- coding: utf-8 -*-
import logging
import uuid
from webob import Response
import webob.dec
LOG = logging.getLogger(__name__)
class Controller():
    def __init__(self):
        pass

    @webob.dec.wsgify
    def __call__(self,req):
        print 'controller call'
        arg_dict = req.environ['wsgiorg.routing_args'][1]
        action = arg_dict.pop('action')
        del arg_dict['controller']
        print req.body
        params = req.environ.get('QUERY_STRING', {})
        print params
        params={}
        # params.update(arg_dict)
        method = getattr(self, action)
        res = method(**params)
        return get_response(res,'200 OK')
class Auth(Controller):
    def __init__(self):
        LOG.info('auth controller init')


    def get_token(self):

        return 'dddddddddd'
    def create_token(self):
        return 'ffffffffff'


def get_response(body,status,headerlist=None):
    return Response(body=body,status=status)

