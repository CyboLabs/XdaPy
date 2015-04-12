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
