import tornado.ioloop
import tornado.web

from controller.rest.main_handler import MainHandler
from controller.rest.story_handler import StoryHandler

if __name__ == "__main__":
    app = tornado.web.Application([
        tornado.web.url(r"/", MainHandler),
        tornado.web.url(r"/story/([0-9]+)", StoryHandler, dict(db="13"), name="story")
    ])

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
