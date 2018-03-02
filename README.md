# GLogging - GrowthIntel Logging

Sensible logging defaults.
Wraps a standard Python logger and delegates method calls to it.

Optionally configure logging to file, screen and logging memory metrics.

## Usage

```
import glogging
log = glogging.GLogging()

log.info("Some log info")
log.debug("I want some extra info %s %s", 'extra metric', 'more debug')
```
