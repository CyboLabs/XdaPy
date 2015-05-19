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
from ..model.pm import Pm as PmModel


class Pms(XdaBase):
    def __init__(self, xda):
        super(Pms, self).__init__(xda)
        self.api = handle_error(self.xda.api.pms)

    def inbox(self, page=1, unread_only=False):
        data = self.api.inbox(page=page, unread_only=unread_only)
        data = data.get('results', [])
        return (PmModel(d) for d in data)

    def sent(self, page=1):
        data = self.api.sent(page=page)
        data = data.get('results', [])
        return (PmModel(d) for d in data)

    # TODO: see forums TODO message regarding handling this data

    def send(self, username, subject, message):
        return self.api.send(username, subject, message)

    def mark_read(self, pm_id):
        return self.api.mark_read(pm_id)

    def mark_unread(self, pm_id):
        return self.api.mark_unread(pm_id)

    def delete_pm(self, pm_id):
        return self.api.delete_pm(pm_id)