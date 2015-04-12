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

from os.path import dirname, abspath
from subprocess import Popen, PIPE

VERSION = (0, 1, 0, 'alpha', 0)


def get_version():
    """Return XdaPy's version."""
    main = '.'.join(str(x) for x in VERSION[:3])
    sub = ''
    if VERSION[3] == 'alpha' and VERSION[4] == 0:
        sub = '.dev-r%s' % get_git_hash()
    elif VERSION[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
        sub = mapping.get(VERSION[3], 'a') + str(VERSION[4])
    return str(main + sub)


def get_git_hash():
    """Return the abbreviated hash of the latest git commit."""
    repo_dir = dirname(dirname(abspath(__file__)))
    git_hash = Popen("git log --pretty=format:'%h' -n 1",
                     stdout=PIPE, stderr=PIPE,
                     shell=True, cwd=repo_dir,
                     universal_newlines=True)
    return git_hash.communicate()[0]
