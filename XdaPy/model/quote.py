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

from .thread import Thread


class Mention(object):
    def __init__(self, data):
        if data is None:
            data = {}
        assert hasattr(data, "get")
        self.page_text = data.get("pagetext", "")
        self.date_line = data.get("dateline", "")
        self.post_id = data.get("postid", "")
        self.type = data.get("type", "")
        self.user_id = data.get("userid", "")
        self.username = data.get("username", "")
        self.quoted_user_id = data.get("quoteduserid", "")
        self.quoted_username = data.get("quotedusername", "")
        self.quoted_user_group_id = data.get("quotedusergroupid", "")
        self.quoted_infraction_group_id = data.get("quotedinfractiongroupid",
                                                   "")
        self.avatar_url = data.get("avatar_url", "")
        self.thread = Thread(data.get("thread"))
