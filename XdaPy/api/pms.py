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
from ..decorators import login_required


class Pms(XdaBase):

    @login_required
    def inbox(self, page=1, unread_only=False):
        method = "GET"
        url = "/v1/pms/inbox"
        d = {"page": page,
             "unread_only": unread_only}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def sent(self, page=1):
        method = "GET"
        url = "/v1/pms/sent"
        d = {"page": page}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def send(self, username, subject, message):
        method = "POST"
        url = "/v1/pms/send"
        d = {"username": username,
             "subject": subject,
             "message": message}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def mark_read(self, pm_id):
        method = "PUT"
        url = "/v1/pms/markread"
        d = {"pmid": pm_id}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def mark_unread(self, pm_id):
        method = "PUT"
        url = "/v1/pms/markunread"
        d = {"pmid": pm_id}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def delete_pm(self, pm_id):
        method = "DELETE"
        url = "/v1/pms"
        d = {"pmid": pm_id}
        return self.xda.requests.basic_request(method, url, body=d)