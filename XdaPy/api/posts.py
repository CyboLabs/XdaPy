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