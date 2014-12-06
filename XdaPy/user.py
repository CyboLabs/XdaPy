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
from .decorators import login_required


class User(XdaBase):

    @login_required
    def user(self):
        method = "GET"
        url = "/v1/user"
        return self.xda.requests.basic_request(method, url)

    @login_required
    def logout(self):
        method = "GET"
        url = "/v1/user/logout"
        self.xda.session.remove_session()
        return self.xda.requests.basic_request(method, url)

    @login_required
    def mentions(self, page=1):
        method = "GET"
        url = "/v1/user/mentions"
        d = {"page": page}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def quotes(self, page=1):
        method = "GET"
        url = "/v1/user/quotes"
        d = {"page": page}
        return self.xda.requests.basic_request(method, url, body=d)

    def userinfo(self, user_id=None):
        if user_id is None:
            return self.user()
        method = "GET"
        url = "/v1/user/userinfo"
        d = {"userid": user_id}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def addmydevice(self, device_id):
        method = "POST"
        url = "/v1/user/addmydevice"
        d = {"deviceid": device_id}
        return self.xda.requests.basic_request(method, url, body=d)

    def login(self, username, password):
        method = "POST"
        url = "/v1/user/login"
        d = {"username": username,
             "password": password}
        return self.xda.requests.make_request(method, url, body=d)

    def register(self, username, password, email,
                 captcha_chal, captcha_resp):
        method = "POST"
        url = "/v1/user/register"
        d = {"username": username,
             "password": password,
             "email": email,
             "captcha_chal": captcha_chal,
             "captcha_resp": captcha_resp}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def updateemail(self, email):
        method = "PUT"
        url = "/v1/user/updateemail"
        d = {"email": email}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def updatepassword(self, cur_password, new_password):
        method = "PUT"
        url = "/v1/user/updatepassword"
        d = {"current_password": cur_password,
             "newpassword": new_password,
             "newpasswordconfirm": new_password}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def delete_mentions(self):
        method = "DELETE"
        url = "/v1/user/notifications/mentions"
        return self.xda.requests.basic_request(method, url)

    @login_required
    def delete_quotes(self):
        method = "DELETE"
        url = "/v1/user/notifications/quotes"
        return self.xda.requests.basic_request(method, url)