# urpatimeout
Extension for setting timeouts in [UltimateRPA](https://www.ultimaterpa.com).   
It helps you with setting up and measuring time limits: 
- for multiple searches, 
- for the whole robotization script.

## Install

```
pip install urpatimeout
```

## Examples

### Setting up a Global Time Limit for Multiple Searches 

```python
import urpatimeout

timeout = urpatimeout.Timeout(10 * 1000)
app = urpa.exec_app("Some_application.exe")
app.find_first(cf.name("Username").text(), timeout=timeout)
app.find_first(cf.name("Password").text(), timeout=timeout)
```

### Setting up a Time Limit for the Whole Robotization Script

```python
import urpatimeout

timeout = urpatimeout.Timeout(60 * 60 * 1000)
while not timeout.is_expired():
	do_something()
```

## Changelog


## Contribute

Issues and pull requests are welcome.
