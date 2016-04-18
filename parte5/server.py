from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop

lista = []


class ListHandler(RequestHandler):
    def get(self):
        self.render('template.html', lista_arg=lista)

    def post(self):
        operacion = self.get_argument('operacion')

        if operacion == 'agregar':
            nombre_elemento = self.get_argument('nombre')
            lista.append(nombre_elemento)

        elif operacion == 'borrar':
            elementos_str = self.get_arguments('elementos')
            elementos = map(int, elementos_str)
            for i in sorted(elementos, reverse=True):
                del lista[i]

        else:
            raise Exception('Operación inválida')

        self.get()

try:
    rutas = [('/lista$', ListHandler)]
    app = Application(rutas, debug=True)
    app.listen(50000)
    IOLoop.instance().start()

except KeyboardInterrupt:
    exit()
