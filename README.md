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
You can turn off logging to screen by passing the kwarg `log_to_screen`:
```python
log = glogging.GLogging(log_to_screen=False)
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
If you prefer, you can use `getLoggerFromPath` to supply the full path:
```python
glogging.getLoggerFromPath('/var/log/api/mylogfile')
# You can supply additional kwargs for GLogging
glogging.getLoggerFromPath('/var/log/api/mylogfile', log_metrics=True)
```

### Logging Resource Usage Metrics

You can log useful system resource usage metrics by default. Set the `log_metrics` kwarg to `True`.
This will log CPU percentage and RAM memory usage.

```python
import glogging
log = glogging.GLogging(log_metrics=True)
log.info("Some log info")
```
will produce:

```bash
2018-03-04 18:39:31,263 [INFO] Mem:11.7MB CPU:13.1% - Some log info (test_glog.py:10)
```

### Retrieving Logger Singletons

You can create a glogging logger like this:
```python
import glogging
logname = "my_log_{0}".format(4569456)
glog = glogging.GLogging(logname=logname)
```

If you only create one logger in your application, then you can easily retrieve it anywhere in the app with:
```python
from glogging import GLogging
# retrieves the "my_log_4569456" logger
glog = GLogging.getLogger()
```
This is convenient if you don't want to pass lognames / loggers around your app.

If you have created multiple loggers in your app, you must supply the logname:
```python
glog = GLogging.getLogger("my_log_4569456")
```
