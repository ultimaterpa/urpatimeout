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

    def __init__(self, timeout: float) -> None:
        """Inicializace instance třídy Timeout.

            Args:
                timeout: float
                    Trvání časového limitu v ms.
        """
        self.timeout = timeout
        self.start = time.monotonic_ns()

    def elapsed(self) -> float:
        """Vrací integer kolik ms uplynulo od začátku časového limitu.

            Returns:
                float
        """
        return (time.monotonic_ns() - self.start) // 1e6

    def remaining(self) -> float:
        """Vrací integer kolik ms ještě zbývá do vypršení časového limitu.

            Returns:
                float
        """
        return self.timeout - self.elapsed()

    def is_expired(self) -> bool:
        """Vrací True pokud časový limit vypršel jinak False.

            Returns:
                bool
        """
        return self.remaining() <= 0
