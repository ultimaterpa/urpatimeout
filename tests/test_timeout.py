import time

import freezegun
import pytest

from urpatimeout import Timeout


TIMEOUTS_MS = (0, 100, 1000, 5000, 30000, 60000, 18000)


@pytest.fixture(params=TIMEOUTS_MS)
def timeout_ms(request):
    return request.param


@pytest.mark.smoke
@freezegun.freeze_time(auto_tick_seconds=5)
def test_remaining_smoke():
    t = Timeout(10000)
    assert t.remaining() == 5000
    assert t.remaining() == 0


@pytest.mark.smoke
@freezegun.freeze_time(auto_tick_seconds=5)
def test_elapsed_smoke():
    t = Timeout(10000)
    assert t.elapsed() == 5000
    assert t.elapsed() == 10000


@pytest.mark.smoke
@freezegun.freeze_time(auto_tick_seconds=5)
def test_expired_smoke():
    t = Timeout(10000)
    assert not t.is_expired()
    assert t.is_expired()


@freezegun.freeze_time(auto_tick_seconds=1)
def test_remaining_type(timeout_ms):
    t = Timeout(timeout_ms)
    assert isinstance(t.remaining(), int)


@freezegun.freeze_time(auto_tick_seconds=1)
def test_elapsed_type(timeout_ms):
    t = Timeout(timeout_ms)
    assert isinstance(t.elapsed(), int)


@freezegun.freeze_time(auto_tick_seconds=1)
def test_is_expired_type(timeout_ms):
    t = Timeout(timeout_ms)
    assert isinstance(t.is_expired(), bool)


@pytest.mark.parametrize(
    "type_error_timeout",
    ([1], {2}, {1: 1}, [], {}, dict(), "", "a", -3.1, 0.0, 1.0, 1e10),
)
def test_type_error(type_error_timeout):
    with pytest.raises(TypeError):
        Timeout(type_error_timeout)


@pytest.mark.parametrize("value_error_timeout", (-1, -1000, -10000))
def test_value_error(value_error_timeout):
    with pytest.raises(ValueError):
        Timeout(value_error_timeout)
