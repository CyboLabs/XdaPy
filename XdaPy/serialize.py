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

# Thin wrapper around the urllib classes, so nowhere else has to
# worry about Python compatibility or even touching httplib

try:
    import json
except ImportError:
    import simplejson as json


def dict_to_str(obj):
    return json.dumps(obj)


def str_to_dict(body):
    if type(body) == bytes:
        body = body.decode()
    return json.loads(body)