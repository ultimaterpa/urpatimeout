import datetime

import freezegun
from hypothesis import given
import hypothesis.strategies as st
import pytest

from urpatimeout import Timeout

FREEZE_DATE = "2000-01-15 00:00:00"


def everything_except(excluded_types):
    return st.from_type(type).flatmap(st.from_type).filter(lambda x: not isinstance(x, excluded_types))


@pytest.mark.smoke
@freezegun.freeze_time(auto_tick_seconds=5)
def test_remaining_input_int():
    t = Timeout(10000)
    assert t.remaining() == 5000
    assert t.remaining() == 0


@pytest.mark.smoke
@freezegun.freeze_time(FREEZE_DATE, auto_tick_seconds=5)
def test_remaining_input_datetime():
    t = Timeout(datetime.datetime(2000, 1, 15, 0, 0, 10))
    assert t.remaining() == 5000
    assert t.remaining() == 0


@pytest.mark.smoke
@freezegun.freeze_time(auto_tick_seconds=5)
def test_elapsed_input_int():
    t = Timeout(10000)
    assert t.elapsed() == 5000
    assert t.elapsed() == 10000


@pytest.mark.smoke
@freezegun.freeze_time(FREEZE_DATE, auto_tick_seconds=5)
def test_elapsed_input_datetime():
    t = Timeout(datetime.datetime(2000, 1, 15, 0, 0, 10))
    assert t.elapsed() == 5000
    assert t.elapsed() == 10000


@pytest.mark.smoke
@freezegun.freeze_time(auto_tick_seconds=5)
def test_expired_input_int():
    t = Timeout(10000)
    assert not t.is_expired()
    assert t.is_expired()


@pytest.mark.smoke
@freezegun.freeze_time(FREEZE_DATE, auto_tick_seconds=5)
def test_expired_input_datetime():
    t = Timeout(datetime.datetime.fromisoformat(FREEZE_DATE) + datetime.timedelta(seconds=10))
    assert not t.is_expired()
    assert t.is_expired()


@pytest.mark.smoke
@freezegun.freeze_time()
def test_past_unsafe_input_int():
    t = Timeout(-1000, past_safe=False)
    assert t.is_expired()


@pytest.mark.smoke
@freezegun.freeze_time(FREEZE_DATE)
def test_past_unsafe_input_datetime():
    t = Timeout(
        datetime.datetime.fromisoformat(FREEZE_DATE) - datetime.timedelta(days=1),
        past_safe=False,
    )
    assert t.is_expired()


@pytest.mark.smoke
@freezegun.freeze_time(auto_tick_seconds=5)
def test_reset():
    t = Timeout(10000)
    assert not t.is_expired()
    t.reset()
    assert not t.is_expired()
    assert t.is_expired()


@pytest.mark.smoke
@freezegun.freeze_time(auto_tick_seconds=5)
def test_reset_and_set():
    t = Timeout(10000)
    assert not t.is_expired()
    t.reset(5000)
    assert t.is_expired()


@given(
    timeout=st.integers(min_value=0)
    | st.datetimes(min_value=datetime.datetime.now(), max_value=datetime.datetime(2038, 1, 1))
)
@freezegun.freeze_time(auto_tick_seconds=1)
def test_remaining_type(timeout):
    t = Timeout(timeout)
    assert isinstance(t.remaining(), int)


@given(
    timeout=st.integers(min_value=0)
    | st.datetimes(min_value=datetime.datetime.now(), max_value=datetime.datetime(2038, 1, 1))
)
@freezegun.freeze_time(auto_tick_seconds=1)
def test_elapsed_type(timeout):
    t = Timeout(timeout)
    assert isinstance(t.elapsed(), int)


@given(
    timeout=st.integers(min_value=0)
    | st.datetimes(min_value=datetime.datetime.now(), max_value=datetime.datetime(2038, 1, 1))
)
@freezegun.freeze_time(auto_tick_seconds=1)
def test_is_expired_type(timeout):
    t = Timeout(timeout)
    assert isinstance(t.is_expired(), bool)


@given(timeout=everything_except((int, datetime.datetime)))
def test_type_error(timeout):
    with pytest.raises(TypeError):
        Timeout(timeout)


@given(
    timeout=st.integers(max_value=-1)
    | st.datetimes(min_value=datetime.datetime(1971, 1, 1), max_value=datetime.datetime.now())
)
def test_value_error(timeout):
    with pytest.raises(ValueError):
        Timeout(timeout)


@given(timeout=everything_except((type(None), int, datetime.datetime)))
def test_reset_type_error(timeout):
    t = Timeout(1000)
    with pytest.raises(TypeError):
        t.reset(timeout)


@given(
    timeout=st.integers(max_value=-1)
    | st.datetimes(min_value=datetime.datetime(1971, 1, 1), max_value=datetime.datetime.now())
)
def test_reset_value_error(timeout):
    t = Timeout(1000)
    with pytest.raises(ValueError):
        t.reset(timeout)


@given(timeout=st.integers(min_value=0))
@freezegun.freeze_time(FREEZE_DATE)
def test_repr(timeout):
    t = Timeout(timeout)
    assert repr(t) == f"<Timeout starts at: '{FREEZE_DATE}' and ends at: '{timeout}' ms>"
