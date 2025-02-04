# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class UserInfoTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.oauth.v1.user_info().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://oauth.twilio.com/v1/userinfo',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "user_sid": "US57cc2449f1b38ed85cf1a43cd8166349",
                "first_name": "Mafalda",
                "last_name": "Rolfson",
                "friendly_name": "mafalda.rolfson+oBgz@ct.sink.twilio.com",
                "email": "mafalda.rolfson+oBgz@ct.sink.twilio.com",
                "url": "https://oauth.twilio.com/v1/userinfo"
            }
            '''
        ))

        actual = self.client.oauth.v1.user_info().fetch()

        self.assertIsNotNone(actual)
