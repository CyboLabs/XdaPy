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

from ..base import XdaBase
from ..decorators import login_required


class Forums(XdaBase):

    def forums(self):
        method = "GET"
        url = "/v1/forums"
        return self.xda.requests.basic_request(method, url)

    def children(self, forum_id):
        method = "GET"
        url = "/v1/forums/children"
        d = {"forumid": forum_id}
        return self.xda.requests.basic_request(method, url, body=d)

    def find_by_device(self, query):
        method = "GET"
        url = "/v1/forums/findbydevice"
        d = {"search": query}
        return self.xda.requests.basic_request(method, url, body=d)

    def general(self):
        method = "GET"
        url = "/v1/forums/general"
        return self.xda.requests.basic_request(method, url)

    def newest(self):
        method = "GET"
        url = "/v1/forums/newest"
        return self.xda.requests.basic_request(method, url)

    @login_required
    def subscribed(self):
        method = "GET"
        url = "/v1/forums/subscribed"
        return self.xda.requests.basic_request(method, url)

    def top(self):
        method = "GET"
        url = "/v1/forums/top"
        return self.xda.requests.basic_request(method, url)

    @login_required
    def subscribe(self, forum_id):
        method = "POST"
        url = "/v1/forums/subscribe"
        d = {"forumid": forum_id}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def mark_read(self, forum_id):
        method = "POST"
        url = "/v1/forums/markread"
        d = {"forumid": forum_id}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def unsubscribe(self, forum_id):
        method = "DELETE"
        url = "/v1/forums/unsubscribe"
        d = {"forumid": forum_id}
        return self.xda.requests.basic_request(method, url, body=d)