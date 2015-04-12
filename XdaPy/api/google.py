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

# Based on https://developers.google.com/accounts/docs/OAuth2ForDevices

from ..base import XdaBase
from ..decorators import check_session


class Google(XdaBase):
    """Handles all the requests for getting Google access token

    to use this, you must first create a project at the developer
    console (https://console.developers.google.com).
    go to "APIs & auth", and disable all APIs. then go to
    credentials, click "Create new Client ID", and select
    "Installed application" -> "Other".
    your Client ID and Client Secret can then be added to the session
    by doing `x.session.google_session.set_client("id", "secret")`.
    """
    def __init__(self, xda):
        super(Google, self).__init__(xda)
        self.host = "accounts.google.com"
        self.scope = "email profile"
        self.session = self.xda.session.google_session

    @check_session(["client_id"])
    def get_user_code(self):
        """Get required data for getting a token

        gets a JSON object with device/user codes, the verification
        url, and the interval for polling times.

        See Also:
            https://developers.google.com/accounts/docs/OAuth2ForDevices#obtainingacode
        """
        method = "POST"
        url = "/o/oauth2/device/code"
        body = {"client_id": self.session.client_id,
                "scope": self.scope}
        return self.xda.requests.basic_enc_request(
            method, url, body=body, host=self.host)

    @check_session(["client_id", "client_secret"])
    def get_tokens(self, device_code):
        """get access and refresh tokens

        gets a JSON object with the access/refresh tokens.

        See Also:
            https://developers.google.com/accounts/docs/OAuth2ForDevices#obtainingatoken
        """
        method = "POST"
        url = "/o/oauth2/token"
        body = {"client_id": self.session.client_id,
                "client_secret": self.session.client_secret,
                "code": device_code,
                "grant_type": "http://oauth.net/grant_type/device/1.0"}
        return self.xda.requests.basic_enc_request(
            method, url, body=body, host=self.host)

    @check_session(["client_id", "client_secret", "refresh_token"])
    def refresh_tokens(self):
        """refresh the access token

        gets a JSON object with the access token in.

        See Also:
            https://developers.google.com/accounts/docs/OAuth2ForDevices#refreshtoken
        """
        method = "POST"
        url = "/o/oauth2/token"
        body = {"client_id": self.session.client_id,
                "client_secret": self.session.client_secret,
                "refresh_token": self.session.refresh_token,
                "grant_type": "refresh_token"}
        return self.xda.requests.basic_enc_request(
            method, url, body=body, host=self.host)
