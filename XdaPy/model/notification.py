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
