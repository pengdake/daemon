#!/usr/bin/env python
from daemon import runner
import commands
import time
from tools.logger import FILE_LOG as LOG 
from tools.logger import STREAM
import utils
import sys

SERVICE = utils.get_conf()
class MyDaemon(object):
    def __init__(self,service):
        self.stdin_path = '/dev/null'
	self.stdout_path = '/dev/null'
	self.stderr_path = '/dev/null'
	self.pidfile_path = '/tmp/%s.pid' % service
	self.pidfile_timeout = 5
        self.service = service
    def run(self):
        eval('Services.'+self.service+'()')

class Services(object):
    @staticmethod
    def memory_monitor():
        service_conf = SERVICE['memory_monitor']
        log_path = service_conf['log_path']
        limit_memory = service_conf['limit_memory']
        latest_log = ''
        while True:
            (status,info) = commands.getstatusoutput('top -b -n 1 > %s' %log_path)
            if not status:
                with open(log_path) as f:
                    lines = f.readlines()
                length = len(lines)
                for key in range(length):
                    if lines[key] == '\n':
                        key += 2
                        line = lines[key].strip()
                        value = ' '.join(filter(lambda x: x,line.split(' ')))
                        result = value.split(' ')
                        break
	        max_memory = result[-3]
                if max_memory > limit_memory:
                    pid = result[0]
                    name = result[-1].strip()
	            (status,info) = commands.getstatusoutput('kill -s 9 %s' %pid)
	            if status:
	                failed_info = 'the memory of %s usage more than %s percent \
	                               and it cannot be killed:%s ' %(name,limit_memory,info)
                        LOG.error(failed_info)
                        if not latest_log or cmp(latest_log,failed_info): 
                            LOG.error(failed_info)
                            latest_log = failed_info
                    else:
                        successed_info = "%s use %s percent is killed successful!" % (name,max_memory)
                        if not latest_log or cmp(latest_log,failed_info):
                            LOG.warn(successed_info)
                            latest_log = successed_info 
            time.sleep(3)
    @staticmethod
    def test():
       while True:
           service_conf = SERVICE['test']
           info = service_conf['info']
           log_path = service_conf['log_path']
           with open(log_path,'w') as f:
               f.write(info)
def action(service):
    my_daemon = MyDaemon(service)    
    daemon_runner = runner.DaemonRunner(my_daemon)
    daemon_runner.daemon_context.files_preserve = [STREAM]
    daemon_runner.do_action()

if __name__ == '__main__':
    action(sys.argv[2])
