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
from ..decorators import login_required


class User(XdaBase):

    @login_required
    def user(self):
        """Return a dict containing info about the logged in user.

        See Also:
            https://api.xda-developers.com/explorer/#!/user/retrieve_get
        """
        method = "GET"
        url = "/v1/user"
        return self.xda.requests.basic_request(method, url)

    @login_required
    def mentions(self, page=1):
        """Return a dict containing the user's mention feed.

        Args:
            page (int, optional): number of pages to return. Defaults to 1.

        See Also:
            https://api.xda-developers.com/explorer/#!/user/mentions_get
        """
        method = "GET"
        url = "/v1/user/mentions"
        d = {"page": page}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def quotes(self, page=1):
        """Return a dict containing the user's quote feed.

        Args:
            page (int, optional): number of pages to return. Defaults to 1.

        See Also:
            https://api.xda-developers.com/explorer/#!/user/quotes_get
        """
        method = "GET"
        url = "/v1/user/quotes"
        d = {"page": page}
        return self.xda.requests.basic_request(method, url, body=d)

    def user_info(self, user_id=None):
        """Return a dict containing public info for a user.

        Args:
            user_id (int, optional): The ID of the user to get the info for.
                Defaults to the logged in user's ID.

        See Also:
            https://api.xda-developers.com/explorer/#!/user/retrieveUserInfo_get
        """
        if user_id is None:
            return self.user()
        method = "GET"
        url = "/v1/user/userinfo"
        d = {"userid": user_id}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def add_my_device(self, device_id):
        """Add a device to "My Devices" for the logged in user.

        Args:
            device_id (int): The ID of the device to add. This is the device's
                top forum ID.

        See Also:
            `forums.find_by_device()`
            https://api.xda-developers.com/explorer/#!/user/retrieveUserInfo_get
        """
        method = "POST"
        url = "/v1/user/addmydevice"
        d = {"deviceid": device_id}
        return self.xda.requests.basic_request(method, url, body=d)

    def google_register(self, access_token, username):
        """Register a new account using Google+

        Args:
            access_token (str): access token for Google+.
            username (str): username.

        See Also:
            https://api.xda-developers.com/explorer/#!/user/createGoogleRegister_post
        """
        method = "POST"
        url = "/v1/user/googleregister"
        d = {"access_token": access_token,
             "username": username}
        return self.xda.requests.basic_request(method, url, body=d)

    def register(self, username, password, email,
                 captcha_chal, captcha_resp):
        """Register a new user.

        Args:
            username (str): desired username.
            password (str): desired password.
            email (str): email address.
            captcha_chal (str): captcha challenge.
            captcha_resp (str): captcha challenge response.

        See Also:
            https://api.xda-developers.com/explorer/#!/user/createRegister_post
        """
        method = "POST"
        url = "/v1/user/register"
        d = {"username": username,
             "password": password,
             "email": email,
             "captcha_chal": captcha_chal,
             "captcha_resp": captcha_resp}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def update_email(self, email):
        """Update the user's email address.

        Args:
            email (str): new email address.

        See Also:
            https://api.xda-developers.com/explorer/#!/user/updateUpdateEmail_put
        """
        method = "PUT"
        url = "/v1/user/updateemail"
        d = {"email": email}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def update_password(self, cur_password, new_password):
        """Update the user's password.

        Args:
            cur_password (str): current password.
            new_password (str): new password.

        See Also:
            https://api.xda-developers.com/explorer/#!/user/updateUpdatePassword_put
        """
        method = "PUT"
        url = "/v1/user/updatepassword"
        d = {"current_password": cur_password,
             "newpassword": new_password,
             "newpasswordconfirm": new_password}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def delete_mentions(self):
        """Clear notifications for mentions.

        See Also:
            https://api.xda-developers.com/explorer/#!/user/mentionNotifications_delete
        """
        method = "DELETE"
        url = "/v1/user/notifications/mentions"
        return self.xda.requests.basic_request(method, url)

    @login_required
    def delete_quotes(self):
        """Clear notifications for quotes.

        See Also:
            https://api.xda-developers.com/explorer/#!/user/quotesNotifications_delete
        """
        method = "DELETE"
        url = "/v1/user/notifications/quotes"
        return self.xda.requests.basic_request(method, url)
