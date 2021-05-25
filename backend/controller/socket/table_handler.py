import socketio


class TableHandler(socketio.AsyncNamespace):
    async def on_connect(self, sid, environ):
        print("on_connect in TableHandler")
        await self.emit('my_response', {'data': 'Connected, from socket handler', 'count': 0}, room=sid)

    async def on_disconnect(self, sid):
        print("on_disconnect in TableHandler from")
        pass
