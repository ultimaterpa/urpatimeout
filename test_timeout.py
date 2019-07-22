import time

import pytest

from timeout import Timeout


TIMEOUTS_MS = (2, 10, 50, 100, 200, 1000, 1500, 5000, 20000)


@pytest.fixture(params=TIMEOUTS_MS)
def timeout_ms(request):
    return request.param, request.param // 2 / 1000, request.param * 1.1 / 1000


def test_remaining(timeout_ms):
    max_ms, first_check_s, second_check_s = timeout_ms
    t = Timeout(max_ms)
    time.sleep(first_check_s)
    assert t.remaining() > 0
    time.sleep(second_check_s)
    assert t.remaining() < 0


def test_is_expired(timeout_ms):
    max_ms, first_check_s, second_check_s = timeout_ms
    t = Timeout(max_ms)
    time.sleep(first_check_s)
    assert t.is_expired() == False
    time.sleep(second_check_s)
    assert t.is_expired()


@pytest.mark.parametrize("more_ms", (5, 20, 40, 300, 1000, 5000, 20000))
def test_elapsed(more_ms):
    delay_s = more_ms / 1000
    less_ms = more_ms + 5
    t = Timeout(1e10)
    time.sleep(delay_s)
    elapsed = t.elapsed()
    assert elapsed >= more_ms and elapsed <= less_ms
