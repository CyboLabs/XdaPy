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
