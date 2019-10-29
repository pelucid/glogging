
import cProfile
import time
import datetime


def timeit(identity=None, logger=None):
    """For timing method execution.

    Identity is an optional string that will be prepended to the method name and time.
    Logger is the logger instance you want to use to output the statement.
    If none, it will print.

    Credit: https://www.andreas-jung.com/contents/a-python-decorator-for-measuring-the-execution-time-of-methods
    """
    def wrap(method):
        def timed(*args, **kw):
            ts = time.time()
            result = method(*args, **kw)
            te = time.time()
            t_formatted = "%r %2.2f sec" % (method.__name__, te-ts)
            if identity:
                t_formatted = "{}: {}".format(identity, t_formatted)
            if logger:
                logger.info(t_formatted)
            else:
                print(t_formatted)
            return result

        return timed
    return wrap


def profile_it(filename, enabled=True):
    """Run cProfile over function (and all called functions)

    Outputs a profile file in the current working directory"""

    def profiled(func):
        def wrapper(*args, **kwargs):
            if not enabled:
                return func(*args, **kwargs)
            profile = cProfile.Profile()
            try:
                profile.enable()
                result = func(*args, **kwargs)
                profile.disable()
                return result
            finally:
                now = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d_%H%M%S')
                profile.dump_stats('{}_{}.txt'.format(filename, now))
        return wrapper
    return profiled
