#!/usr/bin/env python
import utils
import os
import sys

services_list = utils.get_services()
def control_all():
    for service in services_list:
        os.system(" ".join(["./daemon_action.py",sys.argv[1],service]))

if __name__ == "__main__":
    control_all()

