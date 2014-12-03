# Copyright (C) 2014 cybojenix <anthonydking@slimroms.net>
#
# This file is part of XdaPy.
#
# XdaPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# XdaPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with XdaPy.  If not, see <http://www.gnu.org/licenses/>.

# Thin wrapper around the urllib classes, so nowhere else has to
# worry about Python compatibility or even touching httplib

from .base import XdaBase
from . import serialize

try:
    import http.client
    import http.cookies
except ImportError:
    import imp
    import httplib
    import Cookie
    http = imp.new_module('http')
    http.client = httplib
    http.cookies = Cookie


class Requests(XdaBase):
    def __init__(self, xda):
        super(Requests, self).__init__(xda)
        self.methods = ["get", "post", "put", "delete"]

    def make_request(self, method, url, body=None, headers=None):
        if headers is None:
            headers = {}
        method = method.lower()
        if method not in self.methods:
            raise Exception  # Will have it's own exception in future
        headers['Cookie'] = self.xda.session.cookie_str
        if type(body) == dict:
            body = serialize.dict_to_str(body)
        req_func = getattr(self, method)
        return req_func(self.xda.host, url, body, headers)

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
        return {c[0]: c[1].value for c in cookies.items()}

    @staticmethod
    def build_cookie_string(cookie_dict):
        return "; ".join("%s=%s" % (x[0], x[1]) for x in cookie_dict.items())

    @staticmethod
    def get_cookies(r):
        return r.getheader('Set-Cookie')