# timeout
Extension for timeout in [UltimateRPA](https://www.ultimaterpa.com).
You need to have the [UltimateRPA Tools installed](https://www.ultimaterpa.com/documentation/_install.html).  
Helps you with setting up and measuring time limits 
- for multiple searches 
- or for the whole robotization script.


## Examples

### Setting up a Global Time Limit for Multiple Searches 

```python
from timeout import Timeout

search_timeout = Timeout(10000)
app = urpa.exec_app("Some_application.exe")
app.find_first(cf.name("Username").text(), search_timeout)
app.find_first(cf.name("Username").edit(), search_timeout)
```

### Setting up a Time Limit for the Whole Robotization Script

```python
import datetime
from timeout import Timeout

timeout = Timeout(60 * 60 * 1000)
while not timeout.is_expired():
	do_something()
```
