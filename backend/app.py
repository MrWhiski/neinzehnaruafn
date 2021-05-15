import cherrypy


class TarockBackend(object):
    @cherrypy.expose
    def index(self):
        return "Testpenis"


if __name__ == '__main__':
    cherrypy.quickstart(TarockBackend())
