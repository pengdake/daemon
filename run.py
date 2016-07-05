#!/usr/bin/env python
import utils
import os

services_list = utils.get_services()
for service in services_list:
    os.system("./daemon_action.py start "+service)
