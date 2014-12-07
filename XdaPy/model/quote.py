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
        self.quoted_infraction_group_id = data.get("quotedinfractiongroupid", "")
        self.avatar_url = data.get("avatar_url", "")
        self.thread = data.get("thread", {})  # this will link back to a thread object