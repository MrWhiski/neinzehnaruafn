from abc import ABC
from typing import Any

import tornado.web
import tornado.httputil


class MainHandler(tornado.web.RequestHandler):
    def __init__(
            self,
            application: "Application",
            request: tornado.httputil.HTTPServerRequest,
            **kwargs: Any
    ):
        super().__init__(application, request)

    def get(self):
        self.write("HelloWorld")
