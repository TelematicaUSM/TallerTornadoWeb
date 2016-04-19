from tornado.testing import AsyncHTTPTestCase, main

from . import server


class TestApp(AsyncHTTPTestCase):
    def get_app(self):
        return server.new_app()

    def test_lista(self):
        response = self.fetch('/lista')
        self.assertEqual(response.code, 200, 'La respuesta no fué OK (200)')
        self.assertRegex(
            response.body.decode(),
            r'(?ms)'                            # Multiline and dot matches all
            r'(?:'                              # Start group
            r'<input.*? type="checkbox".*?>'    # Input tag
            r'.*?'                              # Maybe a label
            r')'                                # End group
            r'+',                               # One or more times
            'La respuesta no es una lista intercalada de checkboxes y '
            'etiquetas'
        )

if __name__ == '__main__':
    main()
