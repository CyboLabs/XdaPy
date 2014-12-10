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

from .forum import Forum
from .notification import NotificationCount


class User(object):
    def __init__(self, data):
        if data is None:
            data = {}
        assert hasattr(data, "get")
        self.user_id = data.get("userid", "")
        self.username = data.get("username", "")
        self.homepage = data.get("homepage", "")
        self.icq = data.get("icq", "")
        self.aim = data.get("aim", "")
        self.yahoo = data.get("yahoo", "")
        self.msn = data.get("msn", "")
        self.skype = data.get("skype", "")
        self.user_title = data.get("usertitle", "")
        self.join_date = data.get("joindate", "")
        self.posts = data.get("posts", "")
        self.avatar_url = data.get("avatar_url", "")
        self.signature = data.get("signature", "")
        self.post_thanks_user_amount = data.get("post_thanks_user_amount", "")
        self.post_thanks_thanked_posts = data.get("post_thanks_thanked_posts",
                                                  "")
        self.post_thanks_thanked_times = data.get("post_thanks_thanked_times",
                                                  "")
        self.devices = self.load_devices(data.get("devices", []))
        self.email = data.get("email", "")
        self.logout_hash = data.get("logouthash", "")
        self.notifications = NotificationCount(data.get("notifications", {}))

    @staticmethod
    def load_devices(device_data):
        # the device list is actually made up of Forum objects
        data = []
        for d in device_data:
            data.append(Forum(d))
        return data
