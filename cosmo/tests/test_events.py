#/*******************************************************************************
# * Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *       http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.
# *******************************************************************************/

import unittest
import os
from cosmo.tests import get_logger
from cosmo.events import get_cosmo_properties
from cosmo.events import send_event, send_log_event


__author__ = 'elip'

logger = get_logger("EventsTestCase")


class EventsTestCase(unittest.TestCase):

    def test_send_event(self):
        send_event("test", "test", "test", "test", "test")

    def test_send_log_event(self):
        send_log_event("log")

    def test_get_cosmo_properties(self):
        try:
            get_cosmo_properties()
        except RuntimeError:
            pass


