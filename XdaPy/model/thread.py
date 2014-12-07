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
        self.forum_id = data.get("forumid", "")
        self.views = data.get("views", "")
        self.title = data.get("title", "")
        self.page_text = data.get("pagetext", "")
        self.post_username = data.get("postusername", "")
        self.sticky = data.get("sticky", "")
        self.attach = data.get("attach", "")
        self.has_attachment = bool(data.get("has_attachment"))
        self.subscribed = bool(data.get("subscribed"))
        self.total_posts = data.get("total_posts", "")
        self.avatar_url = data.get("avatar_url", "")
        self.unread = bool(data.get("unread"))
        self.open = bool(data.get("open"))
        self.web_uri = data.get("web_uri", "")
