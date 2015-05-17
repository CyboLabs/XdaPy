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

from __future__ import absolute_import

import os


def add_entry_points(xda):
    entry_dir = os.path.dirname(__file__)
    for py in os.listdir(entry_dir):
        if (py.startswith('_') or not py.endswith('.py') or
                os.path.isdir(os.path.join(entry_dir, py))):
            continue

        name = py[:-3]
        klass_name = name.capitalize()

        # turn '_' split names to camelCase
        while klass_name.find('_') > 0:
            i = klass_name.index('_')
            klass_name = klass_name[0:i] + klass_name[i + 1:].capitalize()

        mod = __import__(__name__, fromlist=[name])
        if not hasattr(mod, name):
            continue
        mod = getattr(mod, name)
        if not hasattr(mod, klass_name):
            continue

        setattr(xda, name, getattr(mod, klass_name)(xda))
