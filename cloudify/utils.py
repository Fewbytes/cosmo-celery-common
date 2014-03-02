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

import os

from cloudify.constants import LOCAL_IP_KEY, MANAGER_IP_KEY, \
    MANAGER_REST_PORT_KEY, MANAGER_REST_URL_KEY


def get_local_ip():
    return os.environ[LOCAL_IP_KEY]


def get_manager_ip():
    return os.environ[MANAGER_IP_KEY]


def get_manager_rest_service_port():
    return int(os.environ[MANAGER_REST_PORT_KEY])


def get_manager_rest_url():
    # New style environment: URL. Please migrate to this style.
    # MANAGER_REST_URL is not set by anoyone as of this commit.
    url = os.environ.get(MANAGER_REST_URL_KEY)
    if url is not None:
        return url
    # Old style environment: ip and port. Please stop using.
    return 'http://{0}:{1}'.format(
        get_manager_ip(), get_manager_rest_service_port())


def get_cosmo_properties():
    return {
        "management_ip": get_manager_ip(),
        "ip": get_local_ip()
    }
