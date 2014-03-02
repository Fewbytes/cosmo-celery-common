########
# Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

__author__ = 'idanmo'


import unittest

import os

import cloudify.utils
from cloudify.constants import MANAGER_IP_KEY, \
    MANAGER_REST_PORT_KEY, MANAGER_REST_URL_KEY


class RestApiUrlTest(unittest.TestCase):

    def test_old_style(self):
        e = os.environ
        e.pop(MANAGER_REST_URL_KEY, None)
        e[MANAGER_IP_KEY] = '1.2.3.4'
        e[MANAGER_REST_PORT_KEY] = '50000'
        url = cloudify.utils.get_manager_rest_url()
        self.assertEquals('http://1.2.3.4:50000', url)

    def test_new_style(self):
        e = os.environ
        env_url = 'http://example.com:50001/api'
        e[MANAGER_REST_URL_KEY] = env_url
        e.pop(MANAGER_IP_KEY, None)
        e.pop(MANAGER_REST_PORT_KEY, None)
        url = cloudify.utils.get_manager_rest_url()
        self.assertEquals(env_url, url)
