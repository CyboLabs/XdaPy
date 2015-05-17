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

from getpass import getpass
import sys

from . import requests, session, serialize, api, entry


class Xda(object):
    def __init__(self):
        self.host = "api.xda-developers.com"

        self.session = session.Session(self)
        self.requests = requests.Requests(self)
        self.api = api.Api(self)
        # This will populate Xda with attributes matching the file name
        # of each python file under the entry directory
        entry.add_entry_points(self)

    def login(self, username, password):
        r = self.api.user.login(username, password)
        data = serialize.str_to_dict(r.read())
        if data.get("success", False):
            cookies = self.requests.get_cookies(r)
            self.session.set_session(cookies)
        return data

    def google_login(self, access_token):
        r = self.api.user.google_login(access_token)
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