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

from ..base import XdaBase
from ..decorators import login_required, preview


class Auth(XdaBase):

    def login(self, username, password):
        """Log in.

        Args:
            username (str): username.
            password (str): password.

        See Also:
            https://api.xda-developers.com/explorer/#!/user/createLogin_post
        """
        method = "POST"
        url = "/v1/user/login"
        d = {"username": username,
             "password": password}
        return self.xda.requests.make_request(method, url, body=d)

    @login_required
    def logout(self):
        """Log the user out.

        See Also:
            https://api.xda-developers.com/explorer/#!/user/logout_get
        """
        method = "GET"
        url = "/v1/user/logout"
        self.xda.session.remove_session()
        return self.xda.requests.basic_request(method, url)

    def google_login(self, access_token):
        """Use Google+ Login system.

        Args:
            access_token (str): access token for Google+.

        See Also:
            https://api.xda-developers.com/explorer/#!/user/createGoogleLogin_post
        """
        method = "POST"
        url = "/v1/user/googlelogin"
        d = {"access_token": access_token}
        return self.xda.requests.make_request(method, url, body=d)

    @preview
    def oauth2_start(self):
        method = "GET"
        url = "/v1/oauth2-client"
        return self.xda.requests.make_request(method, url)

    @preview
    def oauth_authorized(self, code):
        method = "GET"
        url = "/v1/oauth2-client/authorized"
        d = {"code": code}
        return self.xda.requests.make_request(method, url, body=d)

    @preview
    def oauth2_get_authorize(self, client_id):
        method = "GET"
        url = "/v1/oauth2-server/authorize"
        d = {}
        return self.xda.requests.make_request(method, url, body=d)

    @preview
    def oauth2_post_authorize(self, client_id):
        method = "POST"
        url = "/v1/oauth2-server/authorize"
        d = {}
        return self.xda.requests.make_request(method, url, body=d)

    @preview
    def oauth2_grant(self, grant_type):
        method = "POST"
        url = "/v1/oauth2-server/grant"
        d = {}
        return self.xda.requests.make_request(method, url, body=d)
