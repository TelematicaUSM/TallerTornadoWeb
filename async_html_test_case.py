import json

from tornado.gen import coroutine
from tornado.httpclient import HTTPRequest
from tornado.httputil import url_concat
from tornado.testing import AsyncHTTPTestCase


class AsyncHTMLTestCase(AsyncHTTPTestCase):
    @coroutine
    def assertIsValidHTML(
            self, response, msg='The response may not contain valid HTML'):
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
        if len(validator_results['messages']) != 0:
            raise AssertionError(
                '{msg}:\n{json}'.format(
                    msg=msg,
                    json=json.dumps(validator_results, indent=2)
                )
            )
