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
from ..model.app import App as AppModel


class Apps(XdaBase):
    def __init__(self, xda):
        super(Apps, self).__init__(xda)
        self.api = self.xda.api.apps

    def promoted(self, limit=None):
        data = self.api.promoted(limit=limit)
        data = data.get('results', [])
        return (AppModel(d) for d in data)
