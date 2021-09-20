"""Urpatimeout is a module for managing timeouts inside UltimateRPA scripts.
https://www.ultimaterpa.com

Features:
It helps you with setting up and measuring time limits:
- set up timeout for multiple searches in UltimateRPA
- set up timeout for part or the whole script
- use `datetime.datetime` as an input
- no 3rd party modules dependencies
"""

from __future__ import annotations

import datetime
import os.path
import time
from typing import Union

import urpautils

START_STAMP_FILE = "start.txt"
TIMEOUT_STAMP_FILE = "timeout.txt"


class Timeout:
    """Class Timeout represents time limit.

    Examples:
        # For example, setting up a global time limit for multiple searches.

        search_timeout = Timeout(5000)
        app.find_first(cf.name("John"), search_timeout)
        app.find_first(cf.name("Doe"), search_timeout)
    """

    def __init__(
        self, timeout: Union[int, datetime.datetime], past_safe: bool = True, persistent: bool = False
    ) -> None:
        """Initialization of instance of class Timeout.

        Args:
            timeout: int or datetime.datetime object
                Duration of time limit in ms or date.
            past_safe: bool
                Set to False to ignore negative timeout value.
            persistent: bool
                Set to True to save timout in case of application crash
        """
        self.start = time.time_ns()
        self.past_safe = past_safe
        self.persistent = persistent
        self.timeout = self._set_timeout(timeout)

    def __repr__(self) -> str:
        start = datetime.datetime.fromtimestamp(self.start / 1_000_000_000)
        return f"<Timeout starts at: '{start}' and ends at: '{self.timeout}' ms>"

    def _set_timeout(self, timeout: Union[int, datetime.datetime]) -> int:
        """Checks, recalculates and returns a time limit.

        Args:
            timeout int or datatime.datetime object
                Duration of the time in ms or date.

        Returns:
            int
        """
        if not isinstance(timeout, (int, datetime.datetime)):
            raise TypeError(f"timeout type must be an int or datetime.datetime, not a '{type(timeout)}'!")
        if isinstance(timeout, datetime.datetime):
            timeout = (int(timeout.timestamp() * 1_000_000_000) - self.start) // 1_000_000
        if timeout < 0 and self.past_safe:
            raise ValueError(
                "timeout value must be a positive int or a datetime.datetime in the future"
                " or consider set a past_safe parameter to False!"
            )
        if self.persistent:
            if os.path.isfile(TIMEOUT_STAMP_FILE) and os.path.isfile(START_STAMP_FILE):
                timeout = int(urpautils.read_txt_file(TIMEOUT_STAMP_FILE))
                self.start = int(urpautils.read_txt_file(START_STAMP_FILE))
            urpautils.write_txt_file(TIMEOUT_STAMP_FILE, str(timeout), mode="w")
            urpautils.write_txt_file(START_STAMP_FILE, str(self.start), mode="w")
        return timeout

    def elapsed(self) -> int:
        """Returns integer which shows how many ms have passed since the start of time limit.

        Returns:
            int
        """
        return (time.time_ns() - self.start) // 1_000_000

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
        print(self.remaining())
        if self.remaining() <= 0:
            urpautils.remove(START_STAMP_FILE)
            urpautils.remove(TIMEOUT_STAMP_FILE)
            return True
        return False

    def reset(self, timeout: Union[None, int, datetime.datetime] = None) -> None:
        """Resets the starting time of the timeout.

        Args:
            timeout: None, int or datetime.datetime
                Omit to keep the time limit or set a new one.
        """
        urpautils.remove(START_STAMP_FILE)
        urpautils.remove(TIMEOUT_STAMP_FILE)
        self.start = time.time_ns()
        if timeout is not None:
            self.timeout = self._set_timeout(timeout)
