# coding: utf-8
import pytest
from httmock import all_requests, response

from freshmail.adapter import FreshMailAdapter


TEST_CONTENT = {'test': True}


@pytest.fixture
def adapter():
    return FreshMailAdapter('0' * 32, '1' * 40)


@all_requests
def response_mock(*args):
    return response(content=TEST_CONTENT)
