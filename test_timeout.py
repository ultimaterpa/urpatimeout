import time

import pytest

from timeout import Timeout


POSITIVE_TIMEOUTS_MS = (2, 10, 50, 100, 200, 1000, 1500, 5000, 20000)
NONPOSITIVE_TIMEOUTS_MS = (-100, -10, -1, 0)


@pytest.fixture(params=POSITIVE_TIMEOUTS_MS)
def timeout_ms(request):
    return request.param


@pytest.fixture(params=POSITIVE_TIMEOUTS_MS)
def timeout_checks(request):
    return request.param, request.param // 2 / 1000, request.param * 1.1 / 1000


def test_remaining(timeout_checks):
    timeout_ms, first_check_s, second_check_s = timeout_checks
    t = Timeout(timeout_ms)
    time.sleep(first_check_s)
    assert t.remaining() > 0
    time.sleep(second_check_s)
    assert t.remaining() < 0


def test_is_expired(timeout_checks):
    timeout_ms, first_check_s, second_check_s = timeout_checks
    t = Timeout(timeout_ms)
    time.sleep(first_check_s)
    assert t.is_expired() is False
    time.sleep(second_check_s)
    assert t.is_expired()


@pytest.mark.parametrize("more_ms", (5, 20, 40, 300, 1000, 5000, 20000))
def test_elapsed(more_ms):
    delay_s = more_ms / 1000
    less_ms = more_ms + 5
    t = Timeout(1000000)
    time.sleep(delay_s)
    elapsed = t.elapsed()
    assert elapsed >= more_ms and elapsed <= less_ms


@pytest.mark.parametrize("wrong_timeout", (-3.1, 0.0, 1.0, 1e10))
def test_init(wrong_timeout):
    with pytest.raises(TypeError):
        Timeout(wrong_timeout)


def test_remaining_type(timeout_ms):
    t = Timeout(timeout_ms)
    assert type(t.remaining()) is int


def test_elapsed_type(timeout_ms):
    t = Timeout(timeout_ms)
    assert type(t.elapsed()) is int


@pytest.mark.parametrize("timeout_ms", NONPOSITIVE_TIMEOUTS_MS)
def test_remaining_negative_value(timeout_ms):
    t = Timeout(timeout_ms)
    assert t.remaining() == 0


@pytest.mark.parametrize("timeout_ms", NONPOSITIVE_TIMEOUTS_MS)
def test_is_expired_negative_value(timeout_ms):
    t = Timeout(timeout_ms)
    assert t.is_expired()
