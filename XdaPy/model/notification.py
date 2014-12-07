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


class NotificationCountType(object):
    def __init__(self, data):
        if data is None:
            data = {}
        assert hasattr(data, "get")
        self.phrase = data.get("phrase", "")
        self.link = data.get("link", "")
        self.order = data.get("order", 0)
        self.total = data.get("total", 0)


class NotificationCount(object):
    def __init__(self, data):
        if data is None:
            data = {}
        assert hasattr(data, "get")
        nct = NotificationCountType
        self.pm_unread = nct(data.get("pmunread"))
        self.friend_requests = nct(data.get("friendreqcount"))
        self.group_join_requests = nct(data.get("socgroupreqcount"))
        self.group_invite_requests = nct(data.get("socgroupinvitecount"))
        self.pic_comments_unread = nct(data.get("pcunreadcount"))
        self.pic_comment_approvals = nct(data.get("pcmoderatedcount"))
        self.mentions = nct(data.get("dbtech_usertag_mentioncount"))
        self.quotes = nct(data.get("dbtech_usertag_quotecount"))
        self.dev_db_updates = nct(data.get("devdbupdates"))
        self.total = data.get("total", 0)
