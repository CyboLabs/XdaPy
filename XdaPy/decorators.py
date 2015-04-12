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



def login_required(func):
    def func_wrapper(self, *args, **kwargs):
        while not self.xda.session.cookies:
            self.xda.default_login()
        return func(self, *args, **kwargs)
    return func_wrapper


def check_session(to_check):
    def wrap(func):
        def func_wrapper(self, *args, **kwargs):
            if self.session:
                s = self.session
            else:
                s = self.xda.session
            for i in to_check:
                try:
                    if not getattr(s, i):
                        raise Exception("%s not set in session" % i)
                except AttributeError:
                    raise Exception("%s not defined in session" % i)
            return func(self, *args, **kwargs)
        return func_wrapper
    return wrap