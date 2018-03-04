import logging
import psutil
import os

class ResourceMetricsFilter(logging.Filter):
    """Implement a resouce usage logging as a filter as per cookbook docs:
    https://docs.python.org/2/howto/logging-cookbook.html#using-filters-to-impart-contextual-information

    This adds Server Resource Usage Metrics to the LogRecord.
    """

    def __init__(self, *args, **kwargs):
        super(ResourceMetricsFilter, self).__init__(*args, **kwargs)
        self.pid = os.getpid()
        self.proc = psutil.Process(self.pid)

    def filter(self, record):
        mem_usage = self.proc.memory_info()
        record.memory = '{:.1f}MB'.format(mem_usage.rss / (2.0**20))
        record.cpu = '{:.1f}%'.format(self.proc.cpu_percent())
        return True
