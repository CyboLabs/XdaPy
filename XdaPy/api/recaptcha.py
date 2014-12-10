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

from ..base import XdaBase


def get_between(body, start, end):
    if type(body) is bytes:
        body = body.decode('utf-8')
    s = body.find(start) + len(start)
    e = body.find(end, s)
    return body[s:e]


class Recaptcha(XdaBase):
    def __init__(self, xda):
        super(Recaptcha, self).__init__(xda)
        self.host = "www.google.com"
        self.public_key = "6LcVyfcSAAAAAG1QaNlcl6o84brVL9sCVF707V8Q"

    def get_challenge(self):
        method = "GET"
        url = "/recaptcha/api/challenge"
        body = {"k": self.public_key}
        d = self.xda.requests.make_request(
            method, url, body=body, host=self.host).read()
        return get_between(d, "challenge : '", "',")

    def get_token(self, t_type, challenge=None):
        if challenge is None:
            challenge = self.get_challenge()
        t_type = t_type.lower()
        assert t_type in ["image", "audio"]

        method = "GET"
        url = "/recaptcha/api/reload"
        body = {"c": challenge,
                "k": self.public_key,
                "type": t_type}
        d = self.xda.requests.make_request(
            method, url, body=body, host=self.host).read()
        return get_between(d, "('", "',")

    def get_image_token(self, challenge=None):
        return self.get_token("image", challenge=challenge)

    def get_audio_token(self, challenge=None):
        return self.get_token("audio", challenge=challenge)

    def get_data(self, t_type, challenge=None, fetch=False):
        t_type = t_type.lower()
        assert t_type in ["image", "audio"]
        if challenge is None:
            challenge = self.get_token(t_type)

        url = "/recaptcha/api/%s" % t_type
        params = "c=%s" % challenge
        url = "?".join((url, params))
        if fetch:
            data = self.xda.requests.get(self.host, url).read()
        else:
            data = None
        return self.host + url, data

    def get_image(self, challenge=None, fetch=False):
        return self.get_data("image", challenge, fetch)

    def get_audio(self, challenge=None, fetch=False):
        return self.get_data("audio", challenge, fetch)
