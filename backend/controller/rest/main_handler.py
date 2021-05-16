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
        #self.db = db

    def get(self):
        self.write('<a href="%s">link to story 1</a>' % self.reverse_url("story", "1"))
        self.write("HelloWorld")
