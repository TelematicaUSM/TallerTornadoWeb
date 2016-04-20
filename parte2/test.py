import json

from tornado.httpclient import HTTPRequest
from tornado.httputil import url_concat
from tornado.testing import AsyncHTTPTestCase, gen_test, main

from . import server


class TestApp(AsyncHTTPTestCase):
    def get_app(self):
        return server.new_app()

    @gen_test
    def test_lista(self):
        url = self.get_url('/lista')
        response = yield self.http_client.fetch(url)

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

        validator_request = HTTPRequest(
            url_concat('https://validator.w3.org/nu/', {'out': 'json'}),
            'POST',
            {'Content-Type': response.headers['Content-Type']},
            response.body
        )
        validator_response = yield self.http_client.fetch(validator_request)
        validator_results = json.loads(
            validator_response.body.decode()
        )
        self.assertEqual(
            len(validator_results['messages']),
            0,
            json.dumps(validator_results, indent=2)
        )


if __name__ == '__main__':
    main()
