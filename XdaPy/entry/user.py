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

from __future__ import absolute_import

from ..base import XdaBase
from ..decorators import handle_error
from ..model.mention import Mention as MentionModel
from ..model.quote import Quote as QuoteModel
from ..model.user import User as UserModel


class User(XdaBase):
    def __init__(self, xda):
        super(User, self).__init__(xda)
        self.api = handle_error(self.xda.api.user)

    def user(self):
        data = self.api.user()
        return UserModel(data)

    def logout(self):
        return self.api.logout()

    def mentions(self, page=1):
        data = self.api.mentions(page=page)
        data = data.get('results', [])
        return (MentionModel(d) for d in data)

    def quotes(self, page=1):
        data = self.api.quotes(page=page)
        data = data.get('results', [])
        return (QuoteModel(d) for d in data)

    def user_info(self, user_id=None):
        data = self.api.user_info(user_id=user_id)
        return UserModel(data)

    def add_my_device(self, device_id):
        return self.api.add_my_device(device_id)

    def login(self, username, password):
        return self.api.login(username, password)

    def register(self, username, password, email,
                 captcha_chal, captcha_resp):
        return self.api.register(username, password, email,
                                 captcha_chal, captcha_resp)

    def update_email(self, email):
        return self.api.update_email(email)

    def update_password(self, cur_password, new_password):
        return self.api.update_password(cur_password, new_password)

    def delete_mentions(self):
        return self.api.delete_mentions()

    def delete_quotes(self):
        return self.api.delete_quotes()