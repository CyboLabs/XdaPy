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

from functools import wraps
import inspect

from .model.error import Error as ErrorModel


def login_required(func):
    @wraps(func)
    def func_wrapper(self, *args, **kwargs):
        while not self.xda.session.cookies:
            self.xda.default_login()
        return func(self, *args, **kwargs)
    return func_wrapper


def check_session(to_check):
    def wrap(func):
        @wraps(func)
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


def handle_error(cls, black_list=None):
    if black_list is None:
        black_list = []

    class Override(object):
        def __init__(self):
            self.__module__ = cls.__module__
            self.__class__.__doc__ = cls.__class__.__doc__
            self.__class__.__module__ = cls.__class__.__module__
            self.__class__.__name__ = cls.__class__.__name__
            self.__class__.__qualname__ = cls.__class__.__qualname__

            self.__dict__ = cls.__dict__

        def __getattribute__(self, item):
            method = getattr(cls, item)
            if (item.startswith('_') or item in black_list or
                    not inspect.isroutine(method)):
                return method
            return wrap_func(method)

    def wrap_func(func):
        @wraps(func)
        def _wrap_func(*args, **kwargs):
            data = func(*args, **kwargs)
            if hasattr(data, 'get'):
                if data.get('error'):
                    return ErrorModel(data),
            return data
        return _wrap_func

    return Override()
