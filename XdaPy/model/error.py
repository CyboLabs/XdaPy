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


class Error(object):
    def __init__(self, data):
        error = data.get('error', {})
        self.code = error.get('code', 0)
        self.message = error.get('message', '')
        self.debug = Debug(data.get('debug', {}))


class Debug(object):
    def __init__(self, debug):
        self.source = debug.get('source', '')

        stages = debug.get('stages', {})
        self.success = stages.get('success', [])
        self.failure = stages.get('failure', [])
