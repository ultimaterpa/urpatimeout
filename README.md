# timeout
Extension for timeout in [UltimateRPA](https://www.ultimaterpa.com)
can be used for setting up and measuring time limits for multiple searches or for the whole robotisation script. 

## Examples

###Setting up a global time limit for multiple searches. 

```python
from timeout import Timeout

search_timeout = Timeout(10000)
app = urpa.exec_app("RpaLoginTest.exe")
app.find_first(cf.name("Username").text(), search_timeout)
app.find_first(cf.name("Username").edit(), search_timeout)
```

###Setting up a time limit for the whole robotisation script.
In this example, expiration of the timeout for the whole script is set to 17:00. 

```python
import datetime
from timeout import Timeout

def set_timeout():
	current_hour = datetime.datetime.now().hour
	timeout = (17 - current_hour) if current_hour < 17 else 0
	return timeout * 3600000

def main():
	timeout = Timeout(set_timeout())
	while not timeout.is_expired():
		do_something()
```
