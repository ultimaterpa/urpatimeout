# urpatimeout
urpatimeout is a module for managing timeouts inside [UltimateRPA](https://www.ultimaterpa.com) scripts.

## Features

It helps you with setting up and measuring time limits:
- set up timeout for multiple searches in UltimateRPA
- set up timeout for part or whole of the script
- use `datetime.datetime` as an input
- no 3rd party modules dependencies

## Install

```
pip install urpatimeout
```

## Examples

### Setting up a Global Timeout for Multiple Searches 

```python
import urpatimeout

timeout = urpatimeout.Timeout(10_000)
app = urpa.exec_app("Some_application.exe")
app.find_first(cf.name("Username").text(), timeout=timeout)
app.find_first(cf.name("Password").text(), timeout=timeout)
```

### Setting up a Timeout for Part of the Script

```python
import urpatimeout

timeout = urpatimeout.Timeout(60 * 60 * 1000)
while not timeout.is_expired():
	do_something()
```

### Using datatime.datetime Object for Setting up the Timeout

```python
import datetime
import urpatimeout

timeout = urpatimeout.Timeout(datetime.datetime(2029, 1, 15))
while not timeout.is_expired():
    do_something_else()
```

### Reseting the Timeout

```python
import urpatimeout
timeout = urpatimeout.Timeout(10_000)
while not timeout.is_expired():
    do_something()
    if this_happened():
        t.reset(5000)
```

## Changelog

[Changelog is here](https://github.com/ultimaterpa/urpatimeout/blob/master/CHANGELOG.md)

## Contribute

Issues and pull requests are welcome.
