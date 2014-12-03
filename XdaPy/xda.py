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

from . import apps, forums, pms, posts, user, requests, session


class Xda(object):
    def __init__(self):
        self.session = session.Session(self)
        self.apps = apps.Apps(self)
        self.forums = forums.Forums(self)
        self.pms = pms.Pms(self)
        self.posts = posts.Posts(self)
        self.user = user.User(self)
        self.requests = requests.Requests(self)

        self.host = "api.xda-developers.com"


