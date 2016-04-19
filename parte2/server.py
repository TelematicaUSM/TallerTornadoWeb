from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop


def new_app():
    rutas = [('/lista$', ListHandler)]
    return Application(rutas, debug=True)


def main():
    try:
        new_app().listen(50000)
        IOLoop.instance().start()

    except KeyboardInterrupt:
        exit()


class ListHandler(RequestHandler):
    def get(self):
        self.render('template.html')


if __name__ == "__main__":
    main()
