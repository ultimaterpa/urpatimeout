"""Modul časového limitu v robotizaci."""

import time


class Timeout:
    """Třída reprezentující časový limit.

    Třídu lze použít pro nastavení a měření časových limitů pro několik hledání nebo celou robotizaci.

    Examples:
        # příklad nastavení globálního časového limit pro několik hledání
        search_timeout = Timeout(5000)
        app.find_first(cf.value("John"), search_timeout)
        app.find_first(cf.name("John"), search_timeout)
    """

    def __init__(self, timeout):
        """Inicializace instance třídy Timeout.

            Args:
                timeout: int
                    Trvání časového limitu v ms.
        """
        self.start = time.monotonic_ns()
        if not isinstance(timeout, int) or timeout <= 0:
            raise TypeError("timeout must be int bigger then 0.")
        self.timeout = timeout

    def elapsed(self):
        """Vrací integer kolik ms uplynulo od začátku časového limitu.

            Returns:
                int
        """
        return (time.monotonic_ns() - self.start) // 1000000

    def remaining(self):
        """Vrací integer kolik ms ještě zbývá do vypršení časového limitu.

            Returns:
                int
        """
        return self.timeout - self.elapsed()

    def is_expired(self):
        """Vrací True pokud časový limit vypršel jinak False.

            Returns:
                bool
        """
        return self.remaining() <= 0
