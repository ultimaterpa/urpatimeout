# urpatimeout

![workflow](https://github.com/ultimaterpa/urpatimeout/actions/workflows/test.yml/badge.svg)
[![PyPi version](https://pypip.in/v/urpatimeout/badge.png)](https://crate.io/packages/urpatimeout/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

urpatimeout is a module for timeouts' management inside [UltimateRPA](https://www.ultimaterpa.com) scripts.

## Features

It helps you with setting up and measuring time limits:
- set up timeout for multiple searches in UltimateRPA
- set up timeout for partial of full script
- use `datetime.datetime` as an input
- no 3rd party modules dependencies required

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
        # This reset the starting time of the timeout. Optionally, you can set a new time limit with t.reset(5000).
        t.reset()
```

### Optional past_safe Parameter


```python
import datetime
import urpatimeout

# This raise ValueError
timeout = urpatimeout.Timeout(datetime.datetime(1990, 1, 1))
# This doesn't raise ValueError
timeout = urpatimeout.Timeout(datetime.datetime(1990, 1, 1), past_safe=False)
```


## Changelog

[Changelog is here](https://github.com/ultimaterpa/urpatimeout/blob/master/CHANGELOG.md)

## Contribute

Issues and pull requests are welcome.
