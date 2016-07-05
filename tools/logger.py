import logging


class MonitorLog(object):
    def __init__(self):
        self.log_path = "/var/log/eayunstack_monitor.log"
        self.log_level = logging.DEBUG
        self.logger = logging.getLogger('MonitorLog')
        self.logger.setLevel(self.log_level)
        self.fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s","%Y-%m-%d %H:%M:%S")
    def file_log(self):
        fh = logging.FileHandler(self.log_path)
        fh.setLevel(self.log_level)
        fh.setFormatter(self.fmt)
        self.logger.addHandler(fh)
        return fh.stream,self.logger
    def stream_log(self):
        ch = logging.StreamHandler()
        ch.setLevel(self.log_level)
        ch.setFormatter(self.fmt)
        self.logger.addHandler(ch)
        return self.logger
   
monitor_obj = MonitorLog()
STREAM,FILE_LOG = monitor_obj.file_log()
#STREAM_LOG = monitor_obj.stream_log()

if __name__ == '__main__':
    STREAM_LOG.info("info")
    STREAM_LOG.debug("debug")
    STREAM_LOG.warn("warn")
    STREAM_LOG.error("error")
