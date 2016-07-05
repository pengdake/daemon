#!/usr/bin/env python
from daemon import runner
import commands
import time
#from tools.logger import FILE_LOG as LOG
import log
import utils

CONF = utils.get_conf()
class MyDaemon(object):
    def __init__(self,service):
        self.stdin_path = '/dev/null'
	self.stdout_path = '/dev/null'
	self.stderr_path = '/dev/null'
	self.pidfile_path = '/tmp/%s.pid' % service
	self.pidfile_timeout = 30
        self.service = service
    def run(self):
        eval('Services.'+self.service+'()')

class Services(object):
    @staticmethod
    def memory_monitor():
        service_conf = CONF['memory_monitor']
        log_path = service_conf['log_path']
        limit_memory = service_conf['limit_memory']
        latest_log = ''
        while True:
            (status,info) = commands.getstatusoutput('top -b -n 1 > %s' %log_path)
            if not status:
                with open(log_path) as f:
                    result = f.readlines()[5].strip().split(' ')
	        max_memory = result[-5]
                if max_memory > limit_memory:
                    pid = result[0]
                    name = result[-1].strip()
	            (status,info) = commands.getstatusoutput('kill -s 9 %s' %pid)
	            if status:
	                failed_info = 'the memory of %s usage more than 80 percent \
	                               and it cannot be killed:%s ' %(name,info)
                        #LOG.error(failed_info)
                        if not latest_log or cmp(latest_log,failed_info): 
                            log.write(failed_info,'error','memory_monitor')
                            latest_log = failed_info
                    else:
                        successed_info = "%s is killed successful!" %name
                        if not latest_log or cmp(latest_log,failed_info):
                            log.write(successed_info,'warn','memory_monitor')
                            latest_log = successed_info 
                        #LOG.warn(successed_info)
            time.sleep(3)
    @staticmethod
    def test():
       while True:
           service_conf = CONF['test']
           info = service_conf['info']
           #log_write(info,"info","test")
           with open('/tmp/hello','w') as f:
               f.write(info)
def action(service):
    my_daemon = MyDaemon(service)
    daemon_runner = runner.DaemonRunner(my_daemon)
    daemon_runner.do_action()

if __name__ == '__main__':
    action("test")
