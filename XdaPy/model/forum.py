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


class Forum(object):
    def __init__(self, data):
        if data is None:
            data = {}
        assert hasattr(data, "get")
        self.title = data.get("title", "")
        self.forum_id = data.get("forumid", -1)
        self.parent_id = data.get("parentid", -1)
        self.forum_slug = data.get("forumslug", "")
        self.subscribed = bool(int(data.get("subscribed", 0)))
        self.image = data.get("image", "")
        self.searchable = data.get("searchable", "")
        self.can_contain_threads = bool(int(data.get("cancontainthreads", 0)))
        self.web_uri = data.get("web_uri", "")

        # these are used in the forum list
        self.children = self.load_children(data.get("children", []))
        self.children_count = data.get("children_count", 0)

        # this is only used for the device list. Make it respect the
        # forum list children too.
        self.has_children = bool(int(data.get("haschildren", 0) or
                                 self.children_count))

        # this is only used the findbydevice method
        self.device = data.get("device", "")

    @staticmethod
    def load_children(children):
        data = []
        for c in children:
            data.append(Forum(c))
        return data
