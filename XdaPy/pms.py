# Copyright (C) 2014 cybojenix <anthonydking@slimroms.net>
#
# This file is part of XdaPy.
#
# XdaPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# XdaPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with XdaPy.  If not, see <http://www.gnu.org/licenses/>.

from .base import XdaBase
from .decorators import login_required


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