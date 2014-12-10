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


class Google(XdaBase):
    def __init__(self, xda):
        super(Google, self).__init__(xda)
        self.host = "accounts.google.com"
        self.scope = "email profile"
        self.session = self.xda.session.google_session

    @check_session(["client_id"])
    def get_user_code(self):
        method = "POST"
        url = "/o/oauth2/device/code"
        body = {"client_id": self.session.client_id,
                "scope": self.scope}
        return self.xda.requests.basic_enc_request(
            method, url, body=body, host=self.host)

    @check_session(["client_id", "client_secret"])
    def get_tokens(self, device_code):
        method = "POST"
        url = "/o/oauth2/token"
        body = {"client_id": self.session.client_id,
                "client_secret": self.session.client_secret,
                "code": device_code,
                "grant_type": "http://oauth.net/grant_type/device/1.0"}
        return self.xda.requests.basic_enc_request(
            method, url, body=body, host=self.host)
