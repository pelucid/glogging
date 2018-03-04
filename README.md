# GLogging - GrowthIntel Logging

Sensible logging defaults.
Wraps a standard Python logger and delegates method calls to it.

Optionally configure logging to file, screen and logging memory metrics.

## Usage

### Basic - Logging to screen

```python
import glogging
log = glogging.GLogging()

log.info("Some log info")
log.debug("I want some extra info %s %s", 'extra metric', 'more debug')
```
will produce:

```bash
2018-03-04 18:28:42,035 [INFO] Some log info (test_glog.py:10)
2018-03-04 18:28:42,035 [DEBUG] I want some extra info extra metric more debug (test_glog.py:11)
```
### Logging to screen and file

If you pass in a logdir, then you get file output. The default logfile name is `growthintel.log`. NB file output does not include source code references:

```python
import glogging
log = glogging.GLogging(logdir='/home/prash/sandpit/glogging/glogging')
```

```bash
2018-03-04 18:28:42,035 [INFO] Some log info
2018-03-04 18:28:42,035 [DEBUG] I want some extra info extra metric more debug
```

### Logging Resource Usage Metrics
```python
import glogging
log = glogging.GLogging(log_metrics=True)
```
