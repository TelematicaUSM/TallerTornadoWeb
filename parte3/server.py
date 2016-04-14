from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop

lista = ['peras', 'papilla', 'puré', 'papas', 'pastel']


class ListHandler(RequestHandler):
    def get(self):
        self.render('template.html', lista_arg=lista)

try:
    rutas = [('/lista$', ListHandler)]
    app = Application(rutas, debug=True)
    app.listen(50000)
    IOLoop.instance().start()

except KeyboardInterrupt:
    exit()
