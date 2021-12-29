from glogging.resource_metrics import ResourceMetricsFilter

import pytest
import re


def test_filter_with_none_record_raises_attribute_error():
    with pytest.raises(AttributeError):
        resource_metrics_filter = ResourceMetricsFilter()
        result = resource_metrics_filter.filter(None)


def test_filter_with_valid_log_record_always_returns_true(valid_log_record):
    resource_metrics_filter = ResourceMetricsFilter()
    result = resource_metrics_filter.filter(valid_log_record)

    assert result


def test_filter_sets_cpu_usage_formatted_as_percentage_to_1dp(valid_log_record):
    percentage_to_one_decimal_place = r'^(\d{0,3}).\d%$'  # e.g. 83.4%

    resource_metrics_filter = ResourceMetricsFilter()
    resource_metrics_filter.filter(valid_log_record)

    assert valid_log_record.cpu is not None
    assert re.match(percentage_to_one_decimal_place, valid_log_record.cpu)


def test_filter_sets_memory_usage_formatted_in_mb_on_log_record(valid_log_record):
    mb_to_one_decimal_place = r'^(\d{0,}).\dMB$'  # e.g. 123.4MB%

    resource_metrics_filter = ResourceMetricsFilter()
    resource_metrics_filter.filter(valid_log_record)

    assert valid_log_record.memory is not None
    assert re.match(mb_to_one_decimal_place, valid_log_record.memory)
