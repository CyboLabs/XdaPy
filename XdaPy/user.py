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

from .base import XdaBase


class User(XdaBase):

    def login(self, username, password):
        method = "POST"
        url = "/v1/user/login"
        d = {"username": username,
             "password": password}
        r = self.xda.requests.make_request(method, url, body=d)
        assert r.status == 200
        cookies = self.xda.requests.get_cookies(r)
        self.xda.session.set_session(username, cookies)

    def logout(self):
        method = "GET"
        url = "/v1/user/logout"
        r = self.xda.requests.make_request(method, url)
        assert r.status == 200
        self.xda.session.remove_session()
