import time

import pytest

from timeout import Timeout


ARG = "timeout_ms,first_check_s,second_check_s"
VALUES = ((10, 0.005, 0.006), (1, 0.0005, 0.0011), (100, 0.05, 0.06), (1000, 0.5, 0.6))


@pytest.mark.parametrize(ARG, VALUES)
def test_remaining(timeout_ms, first_check_s, second_check_s):
    t = Timeout(timeout_ms)
    time.sleep(first_check_s)
    assert t.remaining() > 0
    time.sleep(second_check_s)
    assert t.remaining() < 0


@pytest.mark.parametrize(ARG, VALUES)
def test_is_expired(timeout_ms, first_check_s, second_check_s):
    t = Timeout(timeout_ms)
    time.sleep(first_check_s)
    assert t.is_expired() == False
    time.sleep(second_check_s)
    assert t.is_expired() == True


def test_elapsed():
    t = Timeout(10000)
    time.sleep(0.005)
    assert t.elapsed() >= 5 and t.elapsed() < 7
