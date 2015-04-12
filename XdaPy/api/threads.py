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

from ..base import XdaBase
from ..decorators import login_required


class Threads(XdaBase):

    def threads(self, forum_id, page=1):
        """Return a dict containing the latest threads in a forum.

        Args:
            forum_id (int): the forum's ID to return threads for.
            page (int, optional): number of pages to return. Defaults to 1.

        Return:
            {
                "results" (list): list of threads.
                "total_pages" (int): total pages.
                "per_page" (int): number of threads per page.
                "current_page" (int): current page.
            }

        See Also:
            https://api.xda-developers.com/explorer/#!/threads/retrieve_get
        """
        method = "GET"
        url = "/v1/threads"
        d = {"forumid": forum_id,
             "page": page}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def participated(self, page=1):
        """Return a dict containing threads the user has participated in.

        Args:
            page (int, optional): number of pages to return. Defaults to 1.

        Return:
            {
                "results" (list): list of threads.
                "total_pages" (int): total pages.
                "per_page" (int): number of threads per page.
                "current_page" (int): current page.
            }

        See Also:
            https://api.xda-developers.com/explorer/#!/threads/participated_get
        """
        method = "GET"
        url = "/v1/threads/participated"
        d = {"page": page}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def subscribed(self, page=1, unread_only=False):
        """Return a dict containing subscribed threads.

        Args:
            page (int, optional): number of pages to return. Defaults to 1.
            unread_only (bool, optional): should only unread threads be
                returned? Defaults to False.

        Return:
            {
                "results" (list): list of threads.
                "total_pages" (int): total pages.
                "per_page" (int): number of threads per page.
                "current_page" (int): current page.
            }

        See Also:
            https://api.xda-developers.com/explorer/#!/threads/subscribed_get
        """
        method = "GET"
        url = "/v1/threads/subscribed"
        d = {"page": page,
             "unread_only": unread_only}
        return self.xda.requests.basic_request(method, url, body=d)

    def thread_info(self, thread_id):
        """Return a dict containing info about a thread.

        Args:
            thread_id (int): ID of the thread to get info for.

        See Also:
            https://api.xda-developers.com/explorer/#!/threads/threadInfo_get
        """
        method = "GET"
        url = "/v1/threads/threadinfo"
        d = {"threadid": thread_id}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def new(self, forum_id, title, message):
        """Create a new thread.

        Args:
            forum_id (int): ID of the forum to post in.
            title (str): the title of the thread.
            message (str): the body of the thread.

        See Also:
            https://api.xda-developers.com/explorer/#!/threads/createNew_post
        """
        method = "POST"
        url = "/v1/threads/new"
        d = {"forumid": forum_id,
             "title": title,
             "message": message}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def subscribe(self, thread_id):
        """Subscribe to a thread.

        Args:
            thread_id (int): ID of the thread to subscribe to.

        See Also:
            https://api.xda-developers.com/explorer/#!/threads/createSubscribe_post
        """
        method = "POST"
        url = "/v1/threads/subscribe"
        d = {"threadid": thread_id}
        return self.xda.requests.basic_request(method, url, body=d)

    @login_required
    def unsubscribe(self, thread_id):
        """Unsubscribe from a thread.

        Args:
            thread_id (int): ID of the thread to unsubscribe from.

        See Also:
            https://api.xda-developers.com/explorer/#!/threads/removeUnsubscribe_delete
        """
        method = "POST"
        url = "/v1/threads/unsubscribe"
        d = {"threadid": thread_id}
        return self.xda.requests.basic_request(method, url, body=d)
