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

# Based on https://developers.google.com/accounts/docs/OAuth2ForDevices

from ..base import XdaBase
from ..decorators import check_session
from ..serialize import dict_to_str, str_to_dict
from urllib.parse import urlencode


class Google(XdaBase):
    def __init__(self, xda):
        super(Google, self).__init__(xda)
        self.host = "accounts.google.com"
        self.scope = "email profile"
        self.session = self.xda.session.google_session

    @check_session(["client_id"])
    def get_user_code(self):
        url = "/o/oauth2/device/code"
        body = {"client_id": self.session.client_id,
                "scope": self.scope}
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        body = urlencode(body)
        print(body)
        d = self.xda.requests.post(self.host, url, body=body, headers=headers).read()
        return str_to_dict(d)
