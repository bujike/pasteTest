#! /usr/lib/env python
# -*- coding: utf-8 -*-
from pasteTest.service.auth import controller
class Router ():
    def __init__(self):
        print 'auth init'
    def add_routers(self,mapper):
        auth_controller = controller.Auth()
        mapper.connect('/auth/token',
                       controller=auth_controller,
                       action='get_token',
                       conditions=dict(method=['GET']))
        mapper.connect('/auth/token',
                       controller=auth_controller,
                       action='create_token',
                       conditions=dict(method=['POST']))

