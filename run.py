#!/usr/bin/env python
import utils
from daemon_action import action

#def action_itme():
#    services_list = get_services()
#    for service in services_list:
#        action(service)

#action_item()

services_list = utils.get_services()
for service in services_list:
    action(service)
