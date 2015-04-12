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


class Post(object):
    def __init__(self, data):
        if data is None:
            data = {}
        assert hasattr(data, "get")
        self.post_id = data.get("postid", "")
        self.visible = bool(int(data.get("visible")))
        self.user_id = data.get("userid", "")
        self.title = data.get("title", "")
        self.page_text = data.get("pagetext", "")
        self.username = data.get("username", "")
        self.date_line = data.get("dateline", "")
        self.avatar_url = data.get("avatar_url", "")
        self.thanks_count = data.get("thanks_count", "")
        self.has_thanked = bool(int(data.get("has_thanked")))