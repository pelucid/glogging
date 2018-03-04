# GLogging - GrowthIntel Logging

Sets sensible logging defaults.
Wraps a standard Python logger and delegates method calls to it.

Optionally configure logging to file and logging memory metrics.

## Usage

### Basic - Logging to screen

```python
import glogging
log = glogging.GLogging()

log.info("Some log info")
log.debug("I want some extra info: %s %s", 'API - ', 'more debug info')
```
will produce:

```bash
2018-03-04 18:28:42,035 [INFO] Some log info (test_glog.py:10)
2018-03-04 18:28:42,035 [DEBUG] I want some extra info: API - more debug info (test_glog.py:11)
```
### Logging to screen and file

If you pass in the `logdir` kwarg, then you get file output. The default logfile name is `growthintel.log`. NB file output does not include source code references:

```python
import glogging
log = glogging.GLogging(logdir='/home/prash/sandpit/glogging/glogging')
```
will produce:

```bash
2018-03-04 18:28:42,035 [INFO] Some log info
2018-03-04 18:28:42,035 [DEBUG] I want some extra info: API - more debug info
```
You can customise the logger name / filename, by passing a `logname` kwarg:
```python
log = glogging.GLogging(logname='mylogfile_010118', logdir='/var/log/api')
```

### Logging Resource Usage Metrics

You can log useful system resource usage metrics by default. Set the `log_metrics` kwarg to `True`

```python
import glogging
log = glogging.GLogging(log_metrics=True)
log.info("Some log info")
```

```bash
2018-03-04 18:39:31,263 [INFO] Mem:11.7MB - Some log info (test_glog.py:10)
```
