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

from ..third_party.phpserialize import load as php_load


class Pm(object):
    def __init__(self, data):
        if data is None:
            data = {}
        assert hasattr(data, "get")
        self.pm_id = data.get("pmid", "")
        self.from_user_id = data.get("fromuserid", "")
        self.from_username = data.get("fromusername", "")
        self.title = data.get("title", "")
        self.message = data.get("message", "")
        self.date_line = data.get("dateline", "")
        self.show_signature = bool(int(data.get("showsignature")))
        self.allow_smilie = bool(int(data.get("allowsmilie")))
        self.avatar_url = data.get("avatar_url", "")
        self.message_read = data.get("message_read", "")

        # see http://goo.gl/seoVvh
        self.to_user_array = self.get_php_array(data.get("touserarray", ""))

    @staticmethod
    def get_php_array(array):
        # I've requested for deserializing to take place on the
        # server, since not all languages will be able to do this.
        try:
            d = dict(array)
        except ValueError:
            d = php_load(array)
        return d