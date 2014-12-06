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


class Threads(XdaBase):

    def threads(self, forum_id, page=1):
        method = "GET"
        url = "/v1/threads"
        d = {"forumid": forum_id,
             "page": page}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def participated(self, page=1):
        method = "GET"
        url = "/v1/threads/participated"
        d = {"page": page}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def subscribed(self, page=1, unread_only=False):
        method = "GET"
        url = "/v1/threads/subscribed"
        d = {"page": page,
             "unread_only": unread_only}
        return self.xda.requests.basic_request(method, url, body=d)

    def thread_info(self, thread_id):
        method = "GET"
        url = "/v1/threads/threadinfo"
        d = {"threadid": thread_id}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def new(self, forum_id, title, message):
        method = "POST"
        url = "/v1/threads/new"
        d = {"forumid": forum_id,
             "title": title,
             "message": message}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def subscribe(self, thread_id):
        method = "POST"
        url = "/v1/threads/subscribe"
        d = {"threadid": thread_id}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def unsubscribe(self, thread_id):
        method = "POST"
        url = "/v1/threads/unsubscribe"
        d = {"threadid": thread_id}
        return self.xda.requests.basic_request(method, url, body=d)