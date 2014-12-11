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

from . import requests, session, serialize, api
from getpass import getpass
import sys


class Xda(object):
    def __init__(self, host=None):
        self.host = host or "api.xda-developers.com"

        self.session = session.Session(self)
        self.requests = requests.Requests(self)
        self.api = api.Api(self)

    def login(self, username, password):
        r = self.api.auth.login(username, password)
        data = serialize.str_to_dict(r.read())
        if data.get("success", False):
            cookies = self.requests.get_cookies(r)
            self.session.set_session(cookies)
        return data

    def google_login(self, access_token):
        r = self.api.auth.google_login(access_token)
        data = serialize.str_to_dict(r.read())
        if data.get("success", False):
            cookies = self.requests.get_cookies(r)
            self.session.set_session(cookies)
        return data

    def default_login(self):
        """Call for the `login_required` decorator

        override this to use custom methods for getting user input
        """
        sys.stdout.write("What is your username?\n")
        u = sys.stdin.readline().strip()
        p = getpass("What is your password: ")
        d = self.login(u, p)
        if not d.get("success", False):
            sys.stdout.write("Error while logging in: %s\n" %
                             d.get("error", {}).get("message", "Unknown Error"))