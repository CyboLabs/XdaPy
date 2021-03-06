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

from . import apps, forums, pms, posts, recaptcha, threads, user


class Api(object):
    def __init__(self, xda):
        self.apps = apps.Apps(xda)
        self.forums = forums.Forums(xda)
        self.pms = pms.Pms(xda)
        self.posts = posts.Posts(xda)
        self.user = user.User(xda)
        self.threads = threads.Threads(xda)
        self.recaptcha = recaptcha.Recaptcha(xda)
        # self.google = google.Google(xda)
