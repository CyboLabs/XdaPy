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


def make_request(method, host, url, body=None, headers=None):
    if headers is None:
        headers = {}
    c = http.client.HTTPSConnection(host)
    c.request(method, url, body=body, headers=headers)
    r = c.getresponse()
    return r


def get(host, url, body=None, headers=None):
    r = make_request("GET", host, url, body=body, headers=headers)
    return r


def post(host, url, body=None, headers=None):
    r = make_request("POST", host, url, body=body, headers=headers)
    return r


def put(host, url, body=None, headers=None):
    r = make_request("PUT", host, url, body=body, headers=headers)
    return r


def delete(host, url, body=None, headers=None):
    r = make_request("DELETE", host, url, body=body, headers=headers)
    return r


def parse_cookies(cookie_str):
    """Parse the useful data from Set-Cookie

    Set-Cookie includes a lot of junk which is causing the cookie
    to be broken. Parse the useful data into a dict.
    """
    cookies = http.cookies.SimpleCookie(cookie_str)
    return {c[0]: c[1].value for c in cookies.items()}


def build_cookie_string(cookie_dict):
    return "; ".join("%s=%s" % (x[0], x[1]) for x in cookie_dict.items())