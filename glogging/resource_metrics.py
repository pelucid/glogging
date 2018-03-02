import logging
import psutil
import os

class ResourceMetricsFilter(logging.Filter):
    def __init__(self, *args, **kwargs):
        super(ResourceMetricsFilter, self).__init__(*args, **kwargs)
        self.pid = os.getpid()
        self.proc = psutil.Process(self.pid)

    def filter(self, record):
        mem_usage = self.proc.memory_info()
        record.memory = '{:.1f}MB'.format(mem_usage.rss / (2.0**20))
        return True
