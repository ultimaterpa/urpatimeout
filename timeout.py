"""Modul for time limit in robotisation."""

import time


class Timeout:
    """Class which represent time limit.

    Class is for setting up and messuring time limits for multiple searches or for whole robotisation script.

    Examples:
        # For example, setting up global time limit for mutliple searches.

        search_timeout = Timeout(5000)
        app.find_first(cf.value("John"), search_timeout)
        app.find_first(cf.name("John"), search_timeout)
    """

    def __init__(self, timeout):
        """Initialization of instance of class Timeout. 

            Args:
                timeout: int
                    Duration of time limit in ms.
        """
        self.start = time.monotonic_ns()
        if not isinstance(timeout, int) or timeout <= 0:
            raise TypeError("timeout must be int bigger then 0.")
        self.timeout = timeout

    def elapsed(self):
        """Return integer which show how many ms has passed since start of time limit.

            Returns:
                int
        """
        return (time.monotonic_ns() - self.start) // 1000000

    def remaining(self):
        """Return integer which show how many ms till expiration of time limit.

            Returns:
                int
        """
        return self.timeout - self.elapsed()

    def is_expired(self):
        """Return True if time limit expired.

            Returns:
                bool
        """
        return self.remaining() <= 0
