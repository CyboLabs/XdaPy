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
from .requests import get, post

import json


class User(XdaBase):

    def login(self, username, password):
        url = "/v1/user/login"
        d = {"username": username,
             "password": password}
        r = post(self.xda.host, url, body=json.dumps(d))
        assert r.status == 200
        self.session.set_session(username, r.getheader("Set-Cookie"))

    def logout(self):
        url = "/v1/user/logout"
        r = get(self.xda.host, url)
        assert r.status == 200
        self.session.remove_session()
