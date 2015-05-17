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

from __future__ import absolute_import

from ..base import XdaBase
from ..model.forum import Forum as ForumModel

class Forums(XdaBase):
    def __init__(self, xda):
        super(Forums, self).__init__(xda)
        self.api = self.xda.api.forums

    def forums(self):
        data = self.api.forums()
        data = data.get('results', [])
        return (ForumModel(d) for d in data)

    def children(self, forum_id):
        data = self.api.children(forum_id)
        data = data.get('results', [])
        return (ForumModel(d) for d in data)

    def find_by_device(self, query):
        data = self.api.find_by_device(query)
        data = data.get('results', [])
        return (ForumModel(d) for d in data)

    def general(self):
        data = self.api.general()
        data = data.get('results', [])
        return (ForumModel(d) for d in data)

    def newest(self):
        data = self.api.newest()
        data = data.get('results', [])
        return (ForumModel(d) for d in data)

    def subscribed(self):
        data = self.api.subscribed()
        data = data.get('results', [])
        return (ForumModel(d) for d in data)

    def top(self):
        data = self.api.top()
        data = data.get('results', [])
        return (ForumModel(d) for d in data)

    # TODO: The ones below return a dictionary with success = true in.
    #       This should be handled properly when we do the error handling
    #       implementation later.

    def subscribe(self, forum_id):
        return self.api.subscribe(forum_id)

    def mark_read(self, forum_id):
        return self.api.mark_read(forum_id)

    def unsubscribe(self, forum_id):
        return self.api.unsubscribe(forum_id)