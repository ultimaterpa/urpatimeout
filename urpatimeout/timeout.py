"""Module for time limit in robotization."""

from __future__ import annotations
import time


class Timeout:
    """Class which represents time limit.

    Class is for setting up and measuring time limits for multiple searches or whole robotization script.

    Examples:
        # For example, setting up a global time limit for multiple searches.

        search_timeout = Timeout(5000)
        app.find_first(cf.value("John"), search_timeout)
        app.find_first(cf.name("John"), search_timeout)
    """

    def __init__(self, timeout: int) -> None:
        """Initialization of instance of class Timeout.

            Args:
                timeout: int
                    Duration of time limit in ms.
        """
        self.start = time.time_ns()
        if not isinstance(timeout, int):
            raise TypeError(f"timeout type must be an int, not an '{type(timeout)}'!")
        if timeout < 0:
            raise ValueError(
                f"timeout value must be a positive int, not a '{timeout}'!"
            )
        self.timeout = timeout

    def elapsed(self) -> int:
        """Returns integer which shows how many ms have passed since the start of time limit.

            Returns:
                int
        """
        return (time.time_ns() - self.start) // 1000000

    def remaining(self) -> int:
        """Returns integer which shows how many ms are remaining till the expiration of time limit.

            Returns:
                int
        """
        return self.timeout - self.elapsed()

    def is_expired(self) -> bool:
        """Returns True if time limit expired.

            Returns:
                bool
        """
        return self.remaining() <= 0
