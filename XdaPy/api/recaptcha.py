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


class Recaptcha(XdaBase):
    def __init__(self, xda):
        super(Recaptcha, self).__init__(xda)
        self.host = "www.google.com"
        self.public_key = "6LcVyfcSAAAAAG1QaNlcl6o84brVL9sCVF707V8Q"

    def get_challenge(self):
        url = "/recaptcha/api/challenge"
        params = "k=%s" % self.public_key
        url = "?".join((url, params))
        d = self.xda.requests.get(self.host, url).read()
        start = d.find("challenge : ") + 13
        end = d.find("',\n", start)
        return d[start:end]

    def get_token(self, t_type, challenge=None):
        if challenge is None:
            challenge = self.get_challenge()
        t_type = t_type.lower()
        assert t_type in ["image", "audio"]
        url = "/recaptcha/api/reload"
        params = "c=%s&k=%s&type=%s" % (
            challenge, self.public_key, t_type
        )
        url = "?".join((url, params))
        d = self.xda.requests.get(self.host, url).read()
        start = d.find("('") + 2
        end = d.find("', ", start)
        return d[start:end]

    def get_image_token(self, challenge=None):
        return self.get_token("image", challenge=challenge)

    def get_audio_token(self, challenge=None):
        return self.get_token("audio", challenge=challenge)

    def get_image(self, challenge=None):
        if challenge is None:
            challenge = self.get_image_token()
        url = "/recaptcha/api/image"
        params = "c=%s" % challenge
        url = "?".join((url, params))
        img = self.xda.requests.get(self.host, url).read()
        return url, img

    def get_audio(self, challenge=None):
        if challenge is None:
            challenge = self.get_audio_token()
        url = "/recaptcha/api/audio"
        params = "c=%s" % challenge
        url = "?".join((url, params))
        audio = self.xda.requests.get(self.host, url).read()
        return url, audio