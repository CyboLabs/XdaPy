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
from ..model.post import Post as PostModel
from ..model.smilie import Smilie as SmilieModel
from ..model.thread import Thread as ThreadModel


class Posts(XdaBase):
    def __init__(self, xda):
        super(Posts, self).__init__(xda)
        self.api = self.xda.api.posts

    def posts(self, thread_id, page=1):
        data = self.api.posts(thread_id, page=page)
        thread = data.get('thread', {})
        data = data.get('results', [])
        return (PostModel(d) for d in data), ThreadModel(thread)

    def by_post_id(self, post_id):
        data = self.api.by_post_id(post_id)
        thread = data.get('thread', {})
        data = data.get('results', [])
        return (PostModel(d) for d in data), ThreadModel(thread)

    def new_post(self, thread_id):
        data = self.api.new_post(thread_id)
        thread = data.get('thread', {})
        data = data.get('results', [])
        return (PostModel(d) for d in data), ThreadModel(thread)

    def smilies(self):
        data = self.api.smilies()
        data = data.get('results', [])
        return (SmilieModel(d) for d in data)

    def add_attachment(self, post_id):
        return self.api.add_attachment(post_id)

    def new(self, post_id, message):
        # TODO: handle extracting success and postid properly
        return self.api.new(post_id, message)

    def thanks(self, post_id):
        return self.api.thanks(post_id)

    def delete_thanks(self, post_id):
        return self.api.delete_thanks(post_id)