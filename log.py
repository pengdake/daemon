import time

log_path = "/var/log/eayunstack_monitor.log"

def write(message,level,service):
    log_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    log_message = "  ".join([log_time,level,service,message,'\n'])
    with open(log_path,"a") as log_file:
        log_file.write(log_message)
        
