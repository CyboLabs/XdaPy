# Copyright 2015 cybojenix <anthonydking@slimroms.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Thin wrapper around the urllib classes, so nowhere else has to
# worry about Python compatibility or even touching httplib

from .base import XdaBase
from . import serialize

try:
    import http.client
    import http.cookies
    from urllib.parse import urlencode
except ImportError:
    import imp
    import httplib
    import Cookie
    from urllib import urlencode
    http = imp.new_module('http')
    http.client = httplib
    http.cookies = Cookie


class Requests(XdaBase):
    def __init__(self, xda):
        super(Requests, self).__init__(xda)
        self.methods = ["get", "post", "put", "delete"]

    def make_request(self, method, url, body=None, headers=None, host=None):
        if headers is None:
            headers = {}
        method = method.lower()
        if method not in self.methods:
            raise Exception  # Will have it's own exception in future
        if host is None:
            host = self.xda.host

        # convert the body dictionary to get parameters if method is GET
        if method.lower() in ["get", "delete"] and body:
            get_params = urlencode(body)
            url = "?".join((url, get_params))
            body = None

        headers['Cookie'] = self.xda.session.cookie_str
        if type(body) == dict:
            body = serialize.dict_to_str(body)
        req_func = getattr(self, method)
        return req_func(host, url, body, headers)

    def basic_request(self, *args, **kwargs):
        r = self.make_request(*args, **kwargs)
        return serialize.str_to_dict(r.read())

    def encoded_request(self, *args, **kwargs):
        headers = kwargs.get("headers", {})
        body = kwargs.get("body")
        headers["Content-type"] = "application/x-www-form-urlencoded"
        if type(body) is dict:
            body = urlencode(body)
        kwargs["headers"] = headers
        kwargs["body"] = body
        return self.make_request(*args, **kwargs)

    def basic_enc_request(self, *args, **kwargs):
        r = self.encoded_request(*args, **kwargs)
        return serialize.str_to_dict(r.read())

    @staticmethod
    def get_response(method, host, url, body=None, headers=None):
        if headers is None:
            headers = {}
        c = http.client.HTTPSConnection(host)
        c.request(method, url, body=body, headers=headers)
        r = c.getresponse()
        return r

    def get(self, host, url, body=None, headers=None):
        r = self.get_response("GET", host, url, body=body, headers=headers)
        return r

    def post(self, host, url, body=None, headers=None):
        r = self.get_response("POST", host, url, body=body, headers=headers)
        return r

    def put(self, host, url, body=None, headers=None):
        r = self.get_response("PUT", host, url, body=body, headers=headers)
        return r

    def delete(self, host, url, body=None, headers=None):
        r = self.get_response("DELETE", host, url, body=body, headers=headers)
        return r

    @staticmethod
    def parse_cookies(cookie_str):
        """Parse the useful data from Set-Cookie

        Set-Cookie includes a lot of junk which is causing the cookie
        to be broken. Parse the useful data into a dict.
        """
        cookies = http.cookies.SimpleCookie(cookie_str)
        d = {}
        for c in cookies.items():
            d[c[0]] = c[1].value
        return d

    @staticmethod
    def build_cookie_string(cookie_dict):
        return "; ".join("%s=%s" % (x[0], x[1]) for x in cookie_dict.items())

    @staticmethod
    def get_cookies(r):
        return r.getheader('Set-Cookie')