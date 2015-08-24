# coding: utf-8
import pytest

from freshmail.adapter import FreshMailAdapter


@pytest.fixture
def adapter():
    return FreshMailAdapter('0' * 32, '1' * 40)
