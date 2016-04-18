from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop

lista = []


class ListHandler(RequestHandler):
    def get(self):
        self.render('template.html', lista_arg=lista)

    def post(self):
        nombre_elemento = self.get_argument('nombre')
        lista.append(nombre_elemento)
        self.get()

try:
    rutas = [('/lista$', ListHandler)]
    app = Application(rutas, debug=True)
    app.listen(50000)
    IOLoop.instance().start()

except KeyboardInterrupt:
    exit()
