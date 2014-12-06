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