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
from ..decorators import handle_error
from ..model.thread import Thread as ThreadModel


class Threads(XdaBase):
    def __init__(self, xda):
        super(Threads, self).__init__(xda)
        self.api = handle_error(self.xda.api.threads)

    def threads(self, forum_id, page=1):
        data = self.api.threads(forum_id, page=page)
        data = data.get('results', [])
        return (ThreadModel(d) for d in data)

    def participated(self, page=1):
        data = self.api.participated(page=page)
        data = data.get('results', [])
        return (ThreadModel(d) for d in data)

    def subscribed(self, page=1, unread_only=False):
        data = self.api.subscribed(page=page, unread_only=unread_only)
        data = data.get('results', [])
        return (ThreadModel(d) for d in data)

    def thread_info(self, thread_id):
        data = self.api.thread_info(thread_id)
        return ThreadModel(data)

    def new(self, forum_id, title, message):
        return self.api.new(forum_id, title, message)

    def subscribe(self, thread_id):
        return self.api.subscribe(thread_id)

    def unsubscribe(self, thread_id):
        return self.api.unsubscribe(thread_id)