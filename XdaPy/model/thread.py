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


class Thread(object):
    def __init__(self, data):
        if data is None:
            data = {}
        assert hasattr(data, "get")
        self.thread_id = data.get("threadid", "")
        self.last_post = data.get("lastpost", "")
        self.last_poster = data.get("lastposter", "")
        self.last_post_id = data.get("lastpostid", "")
        self.reply_count = data.get("replycount", "")
        self.first_post_id = data.get("firstpostid", "")
        self.thread_slug = data.get("threadslug", "")
        self.forum_title = data.get("forumtitle", "")
        self.forum_id = data.get("forumid", -1)
        self.views = data.get("views", "")
        self.title = data.get("title", "")
        self.page_text = data.get("pagetext", "")
        self.post_username = data.get("postusername", "")
        self.sticky = data.get("sticky", "")
        self.attach = data.get("attach", "")
        self.has_attachment = bool(int(data.get("has_attachment")))
        self.subscribed = bool(int(data.get("subscribed")))
        self.total_posts = data.get("total_posts", "")
        self.avatar_url = data.get("avatar_url", "")
        self.unread = bool(int(data.get("unread")))
        self.open = bool(int(data.get("open")))
        self.web_uri = data.get("web_uri", "")
