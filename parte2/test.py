from tornado.testing import gen_test, main

from async_html_test_case import AsyncHTMLTestCase
from . import server


class AppTestCase(AsyncHTMLTestCase):
    def get_app(self):
        return server.new_app()

    @gen_test
    def test_lista(self):
        url = self.get_url('/lista')
        response = yield self.http_client.fetch(url)

        yield self.assertIsValidHTML(response)
        self.assertEqual(response.code, 200, 'La respuesta no fue OK (200)')
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
