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


class Posts(XdaBase):

    def posts(self, thread_id, page=1):
        method = "GET"
        url = "/v1/posts"
        d = {"threadid": thread_id,
             "page": page}
        return self.xda.requests.basic_request(method, url, body=d)

    def by_post_id(self, post_id):
        method = "GET"
        url = "/v1/posts/bypostid"
        d = {"postid": post_id}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def new_post(self, thread_id):
        method = "GET"
        url = "/v1/posts/newpost"
        d = {"threadid": thread_id}
        return self.xda.requests.basic_request(method, url, body=d)

    def smilies(self):
        method = "GET"
        url = "/v1/posts/smilies"
        return self.xda.requests.basic_request(method, url)

    def add_attachment(self, post_id):
        method = "POST"
        url = "/v1/posts/addattachment"
        d = {"postid": post_id}
        # return self.xda.requests.basic_request(method, url, body=d)
        raise Exception("Not implemented yet")

    @login_required
    def new(self, post_id, message):
        method = "POST"
        url = "/v1/posts/new"
        d = {"postid": post_id,
             "message": message}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def thanks(self, post_id):
        method = "POST"
        url = "/v1/posts/thanks"
        d = {"postid": post_id}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def delete_thanks(self, post_id):
        method = "DELETE"
        url = "/v1/posts/thanks"
        d = {"postid": post_id}
        return self.xda.requests.basic_request(method, url, body=d)