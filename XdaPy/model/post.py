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