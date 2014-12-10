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


class Session(XdaBase):
    def __init__(self, xda):
        super(Session, self).__init__(xda)
        self.cookies = {}
        self.google_session = GoogleSession()

    @property
    def cookie_str(self):
        return self.xda.requests.build_cookie_string(self.cookies)

    def set_session(self, cookie_str):
        self.cookies = self.xda.requests.parse_cookies(cookie_str)

    def remove_session(self):
        self.cookies = {}


class GoogleSession(object):
    def __init__(self):
        self.client_id = ""
        self.client_secret = ""
        self.access_token = ""
        self.token_type = ""
        self.refresh_token = ""

    def set_client(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def set_token(self, access, refresh, token_type):
        self.access_token = access
        self.token_type = token_type
        self.refresh_token = refresh
