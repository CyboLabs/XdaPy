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
        self.refresh_token = ""

    def set_client(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def set_tokens(self, access, refresh):
        self.access_token = access
        self.refresh_token = refresh

    def set_access_token(self, access):
        self.access_token = access