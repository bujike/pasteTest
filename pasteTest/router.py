#! /usr/lib/env python
# -*- coding: utf-8 -*-
import webob.dec
import webob.exc
import routes
import routes.middleware
import logging

from pasteTest.service.auth import router as auth_router
LOG = logging.getLogger(__name__)
class Router(object):
    """WSGI middleware that maps incoming requests to WSGI apps."""

    def __init__(self, mapper):
        """Create a router for the given routes.Mapper.

        Each route in `mapper` must specify a 'controller', which is a
        WSGI app to call.  You'll probably want to specify an 'action' as
        well and have your controller be an object that can route
        the request to the action-specific method.

        Examples:
          mapper = routes.Mapper()
          sc = ServerController()

          # Explicit mapping of one route to a controller+action
          mapper.connect(None, '/svrlist', controller=sc, action='list')

          # Actions are all implicitly defined
          mapper.resource('server', 'servers', controller=sc)

          # Pointing to an arbitrary WSGI app.  You can specify the
          # {path_info:.*} parameter so the target app can be handed just that
          # section of the URL.
          mapper.connect(None, '/v1.0/{path_info:.*}', controller=BlogApp())

        """
        self.map = mapper
        self._router = routes.middleware.RoutesMiddleware(self._dispatch,
                                                          self.map)

    @webob.dec.wsgify
    def __call__(self, req):
        """Route the incoming request to a controller based on self.map.

        If no match, return a 404.

        """
        return self._router

    @staticmethod
    @webob.dec.wsgify
    def _dispatch(req):
        """Dispatch the request to the appropriate controller.

        Called by self._router after matching the incoming request to a route
        and putting the information into req.environ.  Either returns 404
        or the routed WSGI app's response.

        """
        match = req.environ['wsgiorg.routing_args'][1]
        if not match:
            LOG.info('match fail')

        app = match['controller']
        # action = match['action']
        # if getattr(app,str(action)):
        #     print action
        #     ret = getattr(app,str(action))
        #     return ret()
        return app


def service_app_factory(global_conf, **local_conf):
    mapper = routes.Mapper()
    all_api_router = [auth_router]

    for api_router in all_api_router:
        router_instance = api_router.Router()
        router_instance.add_routers(mapper)
    return Router(mapper)
