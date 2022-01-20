from logging import LogRecord
import logging
import pytest

@pytest.fixture
def valid_log_record():
    return LogRecord('name-of-logger', logging.INFO, 'source.py', 1, 'Message to log', None, None)
