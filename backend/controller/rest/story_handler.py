from abc import ABC
from typing import Any

import tornado.web
from tornado import web
from tornado import httputil


class StoryHandler(tornado.web.RequestHandler):
    def __init__(
        self,
        application: "Application",
        request: httputil.HTTPServerRequest,
        **kwargs: Any
    ):
        super().__init__(application, request)

    def get(self, story_id):
        self.write("this is story %s" % story_id)
