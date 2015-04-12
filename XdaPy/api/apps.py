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

from ..base import XdaBase


class Apps(XdaBase):

    def promoted(self, limit=None):
        method = "GET"
        url = "/v1/apps/promoted"
        # limit is broken on the xda api, so can't test this properly
        d = None if limit else {"limit": limit}
        return self.xda.requests.basic_request(method, url, body=d)