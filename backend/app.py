import sio
import socketio
import tornado.ioloop
import tornado.web

from controller.rest.main_handler import MainHandler
from controller.rest.story_handler import StoryHandler

from controller.socket.table_handler import TableHandler

socket_server = socketio.AsyncServer(async_mode='tornado', cors_allowed_origins='*')

if __name__ == "__main__":
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/story/([0-9]+)", StoryHandler, dict(db="13")),
            (r"/socket.io/", socketio.get_tornado_handler(socket_server))
        ]
    )

    print('Starting Web Application')

    # defining socket namespaces
    socket_server.register_namespace(TableHandler('/'))

    # start server
    app.listen(1234)
    tornado.ioloop.IOLoop.current().start()
