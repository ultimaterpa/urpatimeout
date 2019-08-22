# timeout
Extension for timeout in [UltimateRPA](https://www.ultimaterpa.com)
can be used for setting up and measuring time limits for multiple searches or for the whole robotization script. 

## Examples

Setting up a global time limit for multiple searches. 

```python
from timeout import Timeout

search_timeout = Timeout(10000)
app = urpa.exec_app("RpaLoginTest.exe")
app.find_first(cf.name("Username").text(), search_timeout)
app.find_first(cf.name("Username").edit(), search_timeout)
```

Setting up a time limit for the whole robotization script. 

```python
import datetime
from timeout import Timeout

timeout = Timeout(60 * 60 * 1000)
while not timeout.is_expired():
	do_something()
```
