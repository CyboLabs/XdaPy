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


class ToUser(object):
    def __init__(self, data):
        if data is None:
            data = {}
        assert hasattr(data, "get")
        self.cc = self.key_val_pair(data.get("cc", {}))
        self.bcc = self.key_val_pair(data.get("bcc", {}))

    @staticmethod
    def key_val_pair(data):
        d = []
        for i, u in data.items():
            d.append((i, u))
        return d


class Pm(object):
    def __init__(self, data):
        if data is None:
            data = {}
        assert hasattr(data, "get")
        self.pm_id = data.get("pmid", "")
        self.from_user_id = data.get("fromuserid", "")
        self.from_username = data.get("fromusername", "")
        self.title = data.get("title", "")
        self.message = data.get("message", "")
        self.date_line = data.get("dateline", "")
        self.show_signature = bool(int(data.get("showsignature")))
        self.allow_smilie = bool(int(data.get("allowsmilie")))
        self.avatar_url = data.get("avatar_url", "")
        self.message_read = data.get("message_read", "")

        # see http://goo.gl/seoVvh
        self.to_user_array = data.get("touserarray", "")
        self.to_user = ToUser(data.get("touser", {}))