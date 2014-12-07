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


class Forum(object):
    def __init__(self, data):
        if data is None:
            data = {}
        assert hasattr(data, "get")
        self.title = data.get("title")
        self.forum_id = data.get("forumid")
        self.parent_id = data.get("parentid")
        self.forum_slug = data.get("forumslug")
        self.subscribed = bool(data.get("subscribed"))
        self.image = data.get("image")
        self.searchable = data.get("searchable")
        self.can_contain_threads = bool(data.get("cancontainthreads"))
        self.web_uri = data.get("web_uri")
        self.has_children = bool(data.get("haschildren"))