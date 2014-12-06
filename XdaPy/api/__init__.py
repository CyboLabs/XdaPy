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

from . import apps, forums, pms, posts, threads, user


class Api(object):
    def __init__(self, xda):
        self.apps = apps.Apps(xda)
        self.forums = forums.Forums(xda)
        self.pms = pms.Pms(xda)
        self.posts = posts.Posts(xda)
        self.user = user.User(xda)
        self.threads = threads.Threads(xda)