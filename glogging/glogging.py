"""GI Logging helper."""


import logging
import logging.handlers
import sys
import os
from os.path import join as path_join


# escape codes for colours from:
# https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
STYLES = {
    'bright': '\x1b[1m',
    'reset': '\x1b[0m',
}

COLOURS = {
    'white': '\x1b[37m',
    'blue': '\x1b[34m',
    'yellow': '\x1b[33m',
    'red': '\x1b[31m',
    'back_red': '\x1b[41m'
}

LOG_LEVELS = {
    'INFO': COLOURS['white'],
    'DEBUG': COLOURS['blue'],
    'WARNING': COLOURS['yellow'],
    'ERROR': STYLES['bright'] + COLOURS['yellow'],
    'CRITICAL': STYLES['bright'] + COLOURS['yellow'] + COLOURS['back_red']
}

SCREEN_FORMAT = "%(asctime)s [%(levelname)s]  %(message)s " + "(" + \
                STYLES['bright'] + "%(filename)s" + \
                STYLES['reset'] + ":%(lineno)d)"

FILE_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"


class ColouredFormatter(logging.Formatter):
    """Class for colouring logging messages."""

    def __init__(self, msg):
        super(ColouredFormatter, self).__init__(msg)

    def format(self, record):
        level = record.levelname
        if level in LOG_LEVELS:
            record.levelname = LOG_LEVELS[level] + level + STYLES['reset']
        return logging.Formatter.format(self, record)


class AllWriteRotatingFileHandler(logging.handlers.RotatingFileHandler):
    """Create all log files with write permissions for anyone.
       http://stackoverflow.com/questions/1407474/
    """

    def _open(self):
        # Temporarily set user file mask to a=rwx
        prev_umask = os.umask(0o000)
        f = logging.handlers.RotatingFileHandler._open(self)
        os.umask(prev_umask)
        return f


class GLogging(object):
    """Custom logging class.
       Sets up coloured logging to screen and a file handler.
    """

    def __init__(self, logname="shoover", logdir=None, log_to_screen=True,
                 log_uncaught_exceptions=True):
        """Initialise logger with desired handlers.

        Arguments:
            logname (str): name for the logger
            logdir (str): name of the directory to log to. If none is passed
                           then no file handler is created
            log_to_screen (bool)
            log_uncaught_exceptions (bool): whether to log uncaught exceptions
                                            instead of just writing to stderr
        """
        self.log_dir = logdir
        self.logger = self._create_logger(logname)
        self._setup_logging_levels()

        if logdir:

            self._setup_file_handler()

        if log_to_screen:
            self._setup_stream_handler()

        if log_uncaught_exceptions:
            sys.excepthook = self._log_uncaught_exceptions

    def _create_logger(self, log_name):
        return logging.getLogger(log_name)

    def _setup_logging_levels(self):
        # 'inherit' the logging functionality
        self.debug = self.logger.debug
        self.info = self.logger.info
        self.warning = self.logger.warning
        self.critical = self.logger.critical
        self.error = self.logger.error
        self.exception = self.logger.exception

    def _setup_stream_handler(self):
        colour_formatter = ColouredFormatter(SCREEN_FORMAT)

        log_stream = logging.StreamHandler()
        log_stream.set_name('screen')
        log_stream.setFormatter(colour_formatter)

        self.logger.addHandler(log_stream)

    def _setup_file_handler(self):
        log_filename = path_join(self.log_dir,
                                 '{}.log'.format(self.logger.name))
        ensure_path_exists(log_filename)
        log_filehandler = AllWriteRotatingFileHandler(
            log_filename, 'a', 5 * 1024 * 1024, 10)

        formatter = logging.Formatter(FILE_FORMAT)
        log_filehandler.set_name('file')
        log_filehandler.setFormatter(formatter)

        self.logger.addHandler(log_filehandler)

    def _log_uncaught_exceptions(self, exc_type, exc_value, exc_traceback):
        self.critical('UNCAUGHT EXCEPTION',
                      exc_info=(exc_type, exc_value, exc_traceback))

    def setLevel(self, level):
        if isinstance(level, str):
            level = level.upper()
        self.logger.setLevel(level)

    def setLogLevel(self, level):
        if isinstance(level, str):
            level = level.upper()
        self.setLevel(level)

    @staticmethod
    def getLogger(name):
        return logging.getLogger(name)


def getLoggerFromPath(logpath="/dev/null/shoover", log_uncaught_exceptions=True):
    """
    Convenience method for splitting a full path into a directory and file
    """
    log_split_pos = logpath.rfind('/') + 1

    return GLogging(logname=logpath[log_split_pos:],
                    logdir=logpath[:log_split_pos],
                    log_uncaught_exceptions=log_uncaught_exceptions)


def ensure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
