# urpatimeout
Urpatimeout is a module for managing timeouts inside [UltimateRPA](https://www.ultimaterpa.com) scripts.
It helps you with setting up and measuring time limits:
- for multiple searches
- for the whole or part of the script

## Install

```
pip install urpatimeout
```

## Examples

### Setting up a Global Time Limit for Multiple Searches 

```python
import urpatimeout

timeout = urpatimeout.Timeout(10_000)
app = urpa.exec_app("Some_application.exe")
app.find_first(cf.name("Username").text(), timeout=timeout)
app.find_first(cf.name("Password").text(), timeout=timeout)
```

### Setting up a Time Limit for Part of the Script

```python
import urpatimeout

timeout = urpatimeout.Timeout(60 * 60 * 1000)
while not timeout.is_expired():
	do_something()
```

### Using datatime.datetime for Setting up the Time Limit

```python
import datetime
import urpatimeout

timeout = Timeout(datetime.datetime(2O29, 1, 15)
while not timeout.is_expired():
    do_something_else()
```

## Changelog


## Contribute

Issues and pull requests are welcome.
