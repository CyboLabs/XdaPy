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
from . import serialize

from getpass import getpass
import sys


class User(XdaBase):

    @login_required
    def user(self):
        method = "GET"
        url = "/v1/user"
        r = self.xda.requests.make_request(method, url)
        return serialize.str_to_dict(r.read())

    @login_required
    def logout(self):
        method = "GET"
        url = "/v1/user/logout"
        r = self.xda.requests.make_request(method, url)
        assert r.status == 200
        self.xda.session.remove_session()

    @login_required
    def mentions(self, page=1):
        method = "GET"
        url = "/v1/user/mentions"
        d = {"page": page}
        r = self.xda.requests.make_request(method, url, body=d)
        return serialize.str_to_dict(r.read())

    @login_required
    def quotes(self, page=1):
        method = "GET"
        url = "/v1/user/quotes"
        d = {"page": page}
        r = self.xda.requests.make_request(method, url, body=d)
        return serialize.str_to_dict(r.read())

    def userinfo(self, user_id=None):
        if user_id is None:
            return self.user()
        method = "GET"
        url = "/v1/user/userinfo"
        d = {"userid": user_id}
        r = self.xda.requests.make_request(method, url, body=d)
        return serialize.str_to_dict(r.read())

    @login_required
    def addmydevice(self, device_id):
        method = "POST"
        url = "/v1/user/addmydevice"
        d = {"deviceid": device_id}
        r = self.xda.requests.make_request(method, url, body=d)
        return serialize.str_to_dict(r.read())

    def login(self, username, password):
        method = "POST"
        url = "/v1/user/login"
        d = {"username": username,
             "password": password}
        r = self.xda.requests.make_request(method, url, body=d)
        assert r.status == 200
        cookies = self.xda.requests.get_cookies(r)
        self.xda.session.set_session(username, cookies)

    def register(self, username, password, email,
                 captcha_chal, captcha_resp):
        method = "POST"
        url = "/v1/user/register"
        d = {"username": username,
             "password": password,
             "email": email,
             "captcha_chal": captcha_chal,
             "captcha_resp": captcha_resp}
        r = self.xda.requests.make_request(method, url, body=d)
        return serialize.str_to_dict(r.read())

    @login_required
    def updateemail(self, email):
        method = "PUT"
        url = "/v1/user/updateemail"
        d = {"email": email}
        r = self.xda.requests.make_request(method, url, body=d)
        return serialize.str_to_dict(r.read())

    @login_required
    def updatepassword(self, cur_password, new_password):
        method = "PUT"
        url = "/v1/user/updatepassword"
        d = {"current_password": cur_password,
             "newpassword": new_password,
             "newpasswordconfirm": new_password}
        r = self.xda.requests.make_request(method, url, body=d)
        return serialize.str_to_dict(r.read())

    @login_required
    def delete_mentions(self):
        method = "DELETE"
        url = "/v1/user/notifications/mentions"
        r = self.xda.requests.make_request(method, url, body=d)
        return serialize.str_to_dict(r.read())

    @login_required
    def delete_quotes(self):
        method = "DELETE"
        url = "/v1/user/notifications/quotes"
        r = self.xda.requests.make_request(method, url, body=d)
        return serialize.str_to_dict(r.read())


    def default_login(self):
        """Call for the `login_required` decorator

        override this to use custom methods for getting user input
        """
        sys.stdout.write("What is your username?\n")
        u = sys.stdin.readline().strip()
        p = getpass("What is your password: ")
        self.login(u, p)